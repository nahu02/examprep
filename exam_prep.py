#!/usr/bin/env python3
"""
Exam Preparation Script
Uses Perplexity API to generate study scaffolds from PDF sources.
"""

import os
import json
import hashlib
import requests
import time
from pathlib import Path
from typing import Dict, Any, List, Literal, Optional
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
import yaml

try:
    import fitz  # PyMuPDF
except ImportError:
    print("ERROR: PyMuPDF not installed. Run: pip install pymupdf")
    exit(1)


# ============================================================================
# CONFIGURATION & UTILITIES
# ============================================================================


def load_env_file():
    """Load environment variables from .env file if it exists."""
    env_path = Path(__file__).parent / ".env"
    if env_path.exists():
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, value = line.split("=", 1)
                    os.environ[key.strip()] = value.strip()


def get_file_hash(file_path: Path) -> str:
    """Calculate SHA256 hash of a file."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


def load_prompt(prompt_name: str) -> str:
    """Load a prompt template from the prompts/ directory."""
    prompt_path = Path(__file__).parent / "prompts" / f"{prompt_name}.txt"
    if not prompt_path.exists():
        raise FileNotFoundError(f"Prompt file not found: {prompt_path}")
    return prompt_path.read_text()


# ============================================================================
# PERPLEXITY API CLIENT
# ============================================================================


def call_perplexity(
    messages: List[Dict[str, str]],
    model: Literal["sonar", "sonar-pro"] = "sonar",
    temperature: float = 0.0,
    response_format: Optional[Dict[str, str]] = None,
    max_retries: int = 3,
) -> str:
    """
    Call Perplexity API with proper error handling and exponential backoff.

    Args:
        messages: List of message dicts with 'role' and 'content'
        model: 'sonar' (cheap, fast) or 'sonar-pro' (better quality)
        temperature: Randomness (0.0 = deterministic)
        response_format: Optional dict like {"type": "json_object"}
        max_retries: Number of retry attempts on failure

    Returns:
        Response content as string
    """
    api_key = os.environ.get("PERPLEXITY_API_KEY")
    if not api_key:
        raise ValueError(
            "PERPLEXITY_API_KEY environment variable not set. "
            "Create a .env file with: PERPLEXITY_API_KEY=your_key_here"
        )

    payload = {"model": model, "messages": messages, "temperature": temperature}
    if response_format:
        payload["response_format"] = response_format

    for attempt in range(max_retries + 1):
        try:
            response = requests.post(
                "https://api.perplexity.ai/chat/completions",
                json=payload,
                headers={
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json",
                },
                timeout=120,
            )
            response.raise_for_status()
            data = response.json()
            return data["choices"][0]["message"]["content"]
        except requests.exceptions.HTTPError as e:
            # Handle rate limiting with exponential backoff
            if e.response.status_code == 429:
                if attempt < max_retries:
                    wait_time = (2**attempt) * 2  # 2s, 4s, 8s
                    print(f"  ⚠ Rate limit (429), waiting {wait_time}s...")
                    time.sleep(wait_time)
                    continue
                else:
                    raise Exception(
                        f"Rate limit exceeded after {max_retries + 1} attempts"
                    )
            else:
                # Other HTTP errors
                if attempt < max_retries:
                    print(f"  ⚠ API error ({e.response.status_code}), retrying...")
                    time.sleep(1)
                    continue
                else:
                    raise Exception(
                        f"API call failed after {max_retries + 1} attempts: {e}"
                    )
        except Exception as e:
            if attempt < max_retries:
                print(f"  ⚠ API error, retrying... ({e})")
                time.sleep(1)
                continue
            else:
                raise Exception(
                    f"API call failed after {max_retries + 1} attempts: {e}"
                )


# ============================================================================
# PHASE 1: PDF TEXT EXTRACTION
# ============================================================================


def extract_pdf_text(pdf_path: Path, cache_dir: Path) -> tuple[str, int]:
    """
    Extract text from PDF page-by-page and cache results.

    Returns:
        (pdf_hash, total_pages)
    """
    # Calculate PDF hash
    pdf_hash = get_file_hash(pdf_path)
    pdf_cache_dir = cache_dir / "extracted" / pdf_hash
    metadata_path = pdf_cache_dir / "metadata.json"

    # Check if already extracted
    if metadata_path.exists():
        with open(metadata_path) as f:
            metadata = json.load(f)
            total_pages = metadata["total_pages"]

            # Verify all page files exist
            all_exist = all(
                (pdf_cache_dir / f"page_{i + 1:03d}.txt").exists()
                for i in range(total_pages)
            )

            if all_exist:
                print(f"  ✓ Using cached extraction ({total_pages} pages)")
                return pdf_hash, total_pages

    # Extract text
    print(f"  📄 Extracting {pdf_path.name}...", end=" ", flush=True)
    pdf_cache_dir.mkdir(parents=True, exist_ok=True)

    doc = fitz.open(pdf_path)
    total_pages = len(doc)

    for page_num in range(total_pages):
        page = doc[page_num]
        text = page.get_text("text", sort=True)
        page_file = pdf_cache_dir / f"page_{page_num + 1:03d}.txt"
        page_file.write_text(text, encoding="utf-8")

    doc.close()

    # Save metadata
    metadata = {
        "pdf_path": str(pdf_path),
        "pdf_name": pdf_path.name,
        "total_pages": total_pages,
        "extracted_at": datetime.now().isoformat(),
        "file_hash": pdf_hash,
    }
    with open(metadata_path, "w") as f:
        json.dump(metadata, f, indent=2)

    print(f"{total_pages} pages")
    return pdf_hash, total_pages


# ============================================================================
# PHASE 2: PAGE CLASSIFICATION
# ============================================================================


def classify_pages(
    pdf_hash: str,
    pdf_name: str,
    total_pages: int,
    spec: Dict[str, Any],
    cache_dir: Path,
    max_workers: int = 3,
    delay_between_batches: float = 3,
) -> List[Dict[str, Any]]:
    """
    Classify each page into subtopics using Perplexity API.
    Uses parallel processing optimized for 50 RPM rate limit.

    With max_workers=5 and delay_between_batches=0.1, we get:
    - ~6 requests every 0.6 seconds = ~10 requests/sec = ~600/min (well within limits)
    - But effectively ~50 RPM sustained due to API response times

    Returns:
        List of classification results
    """
    labels_file = cache_dir / "labels" / f"{pdf_hash}.jsonl"
    labels_file.parent.mkdir(parents=True, exist_ok=True)

    # Load existing labels
    existing_labels = {}
    if labels_file.exists():
        with open(labels_file) as f:
            for line in f:
                if line.strip():
                    label_data = json.loads(line)
                    existing_labels[label_data["page"]] = label_data

    # Check if all pages are labeled
    if len(existing_labels) == total_pages:
        print("  ✓ All pages already labeled")
        return list(existing_labels.values())

    # Load prompt template
    prompt_template = load_prompt("classify_page")

    # Prepare subtopics list
    subtopics_list = []
    for subtopic in spec["subtopics"]:
        subtopics_list.append(
            f"**{subtopic['id']}**: {subtopic['title']} - {subtopic['description']}"
        )
    subtopics_text = "\n".join(subtopics_list)

    # Classify each page
    pdf_cache_dir = cache_dir / "extracted" / pdf_hash

    print(
        f"  🏷️  Classifying pages from {pdf_name} (parallel, {max_workers} workers)..."
    )

    # Collect pages that need classification
    pages_to_classify = []
    for page_num in range(1, total_pages + 1):
        if page_num not in existing_labels:
            pages_to_classify.append(page_num)

    if not pages_to_classify:
        return list(existing_labels.values())

    # Get valid subtopic IDs for validation
    valid_labels = {subtopic["id"] for subtopic in spec["subtopics"]}
    valid_labels.add("IRRELEVANT")

    # Define classification function for a single page
    def classify_single_page(page_num: int, retry_count: int = 0) -> Dict[str, Any]:
        """Classify a single page and return the label data."""
        max_classification_retries = 3

        # Load page text
        page_file = pdf_cache_dir / f"page_{page_num:03d}.txt"
        page_text = page_file.read_text(encoding="utf-8")

        # Skip empty or very short pages
        if len(page_text.strip()) < 50:
            return {
                "page": page_num,
                "label": "IRRELEVANT",
                "confidence": 1.0,
                "rationale": "Page too short or empty",
                "classified_at": datetime.now().isoformat(),
            }

        # Prepare prompt
        prompt = prompt_template.format(
            subject=spec["subject"],
            exam_format=spec["exam_format"],
            subtopics_list=subtopics_text,
            page_text=page_text[:4000],  # Limit to avoid token limits
        )

        # Call API
        try:
            # Define JSON schema for classification response
            classification_schema = {
                "type": "object",
                "properties": {
                    "rationale": {"type": "string"},
                    "label": {"type": "string"},
                    "confidence": {"type": "number"},
                },
                "required": ["rationale", "label", "confidence"],
                "additionalProperties": False,
            }

            response = call_perplexity(
                messages=[{"role": "user", "content": prompt}],
                model="sonar",
                temperature=0.0,
                response_format={
                    "type": "json_schema",
                    "json_schema": {"schema": classification_schema},
                },
            )

            # Parse response
            label_info = json.loads(response)
            label = label_info["label"]

            # Validate label is in spec subtopics
            if label not in valid_labels:
                if retry_count < max_classification_retries:
                    print(
                        f"\n    ⚠ Invalid label '{label}' for page {page_num}, retrying ({retry_count + 1}/{max_classification_retries})..."
                    )
                    time.sleep(2)  # Wait before retry
                    return classify_single_page(page_num, retry_count + 1)
                else:
                    print(
                        f"\n    ⚠ Invalid label '{label}' after {max_classification_retries} retries, marking as IRRELEVANT"
                    )
                    return {
                        "page": page_num,
                        "label": "IRRELEVANT",
                        "confidence": 0.0,
                        "rationale": f"Invalid label returned: {label}",
                        "classified_at": datetime.now().isoformat(),
                    }

            return {
                "page": page_num,
                "label": label,
                "confidence": label_info["confidence"],
                "rationale": label_info["rationale"],
                "classified_at": datetime.now().isoformat(),
            }

        except Exception as e:
            # Retry on any error up to max_classification_retries
            if retry_count < max_classification_retries:
                wait_time = (retry_count + 1) * 2
                print(f"\n    ⚠ Error classifying page {page_num}: {e}")
                print(
                    f"    ⏳ Retrying in {wait_time}s ({retry_count + 1}/{max_classification_retries})..."
                )
                time.sleep(wait_time)
                return classify_single_page(page_num, retry_count + 1)
            else:
                print(
                    f"\n    ❌ Failed to classify page {page_num} after {max_classification_retries} retries"
                )
                # Only mark as irrelevant after exhausting all retries
                return {
                    "page": page_num,
                    "label": "IRRELEVANT",
                    "confidence": 0.0,
                    "rationale": f"Classification failed after {max_classification_retries} retries: {str(e)}",
                    "classified_at": datetime.now().isoformat(),
                }

    # Process pages in parallel with rate limiting
    results_dict = dict(existing_labels)  # Start with existing labels
    completed_count = len(existing_labels)

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit initial batch of tasks
        futures = []
        pages_iter = iter(pages_to_classify)

        # Start with max_workers initial tasks
        for _ in range(min(max_workers, len(pages_to_classify))):
            try:
                page_num = next(pages_iter)
                future = executor.submit(classify_single_page, page_num)
                futures.append((future, page_num))
            except StopIteration:
                break

        # Process completed tasks and submit new ones with delay
        while futures:
            # Wait for at least one future to complete
            done_futures = []
            for future, page_num in futures:
                if future.done():
                    done_futures.append((future, page_num))

            # If nothing done yet, wait a bit
            if not done_futures:
                time.sleep(0.1)
                continue

            # Process completed futures
            for future, page_num in done_futures:
                futures.remove((future, page_num))

                try:
                    label_data = future.result()
                    results_dict[page_num] = label_data

                    # Append to JSONL file (thread-safe with separate writes)
                    with open(labels_file, "a") as f:
                        f.write(json.dumps(label_data) + "\n")

                    completed_count += 1
                    print(
                        f"\r    Progress: {completed_count}/{total_pages} | Page {page_num}: {label_data['label']}",
                        end="",
                        flush=True,
                    )

                except Exception as e:
                    print(f"\n    ⚠ Unexpected error processing page {page_num}: {e}")

                # Submit a new task with delay to stay within rate limits
                # 50 RPM = 0.83 requests/sec, so 1.2s between requests is safe
                try:
                    new_page_num = next(pages_iter)
                    time.sleep(delay_between_batches)
                    new_future = executor.submit(classify_single_page, new_page_num)
                    futures.append((new_future, new_page_num))
                except StopIteration:
                    pass  # No more pages to process

    print()  # New line after progress

    # Return results in page order
    return [results_dict[i] for i in range(1, total_pages + 1)]


# ============================================================================
# PHASE 3: SINGLE-TOPIC PDF DETECTION
# ============================================================================


def detect_single_topic_pdfs(
    pdf_metadata_list: List[Dict[str, Any]], subject_name: str, cache_dir: Path
) -> None:
    """
    Detect PDFs that primarily cover a single topic.
    Updates subject-level metadata file.
    """
    subject_meta_file = cache_dir / "labels" / f"{subject_name}.jsonl"

    for pdf_meta in pdf_metadata_list:
        pdf_hash = pdf_meta["hash"]
        pdf_name = pdf_meta["name"]
        labels = pdf_meta["labels"]

        # Count labels (exclude IRRELEVANT)
        label_counts = {}
        for label_data in labels:
            label = label_data["label"]
            if label != "IRRELEVANT":
                label_counts[label] = label_counts.get(label, 0) + 1

        total_relevant = sum(label_counts.values())

        if total_relevant == 0:
            is_single_topic = False
            dominant_topic = None
            coverage_percent = 0.0
        else:
            # Find dominant topic
            dominant_topic = max(label_counts, key=label_counts.get)
            dominant_count = label_counts[dominant_topic]
            coverage_percent = (dominant_count / total_relevant) * 100
            is_single_topic = coverage_percent >= 85.0

        # Store metadata
        meta_entry = {
            "source_pdf_name": pdf_name,
            "hash": pdf_hash,
            "is_single_topic": is_single_topic,
            "dominant_topic": dominant_topic,
            "coverage_percent": round(coverage_percent, 1),
            "analyzed_at": datetime.now().isoformat(),
        }

        # Append to subject metadata
        with open(subject_meta_file, "a") as f:
            f.write(json.dumps(meta_entry) + "\n")

        if is_single_topic:
            print(
                f"  📊 {pdf_name}: Single-topic PDF ({dominant_topic}, {coverage_percent:.1f}%)"
            )


# ============================================================================
# PHASE 4: SCAFFOLD GENERATION
# ============================================================================


def generate_scaffolds(
    spec: Dict[str, Any],
    pdf_metadata_list: List[Dict[str, Any]],
    cache_dir: Path,
    output_dir: Path,
) -> Dict[str, int]:
    """
    Generate study scaffolds for each subtopic.

    Returns:
        Dict mapping subtopic_id to number of pages used
    """
    print(f"\n  📝 Generating scaffolds...")

    output_dir.mkdir(parents=True, exist_ok=True)

    # Load scaffold prompt template
    scaffold_template = load_prompt("generate_scaffold")

    # Group pages by subtopic
    subtopic_pages: Dict[
        str, List[tuple[str, int, str]]
    ] = {}  # subtopic_id -> [(pdf_name, page_num, text)]

    for pdf_meta in pdf_metadata_list:
        pdf_hash = pdf_meta["hash"]
        pdf_name = pdf_meta["name"]
        pdf_cache_dir = cache_dir / "extracted" / pdf_hash

        for label_data in pdf_meta["labels"]:
            label = label_data["label"]
            if label == "IRRELEVANT":
                continue

            page_num = label_data["page"]
            page_file = pdf_cache_dir / f"page_{page_num:03d}.txt"
            page_text = page_file.read_text(encoding="utf-8")

            if label not in subtopic_pages:
                subtopic_pages[label] = []
            subtopic_pages[label].append((pdf_name, page_num, page_text))

    # Generate scaffold for each subtopic
    stats = {}

    for subtopic in spec["subtopics"]:
        subtopic_id = subtopic["id"]
        subtopic_title = subtopic["title"]
        subtopic_desc = subtopic["description"]

        if subtopic_id not in subtopic_pages:
            print(f"    ⚠ Skipping {subtopic_id}: no pages found")
            stats[subtopic_id] = 0
            continue

        pages = subtopic_pages[subtopic_id]
        stats[subtopic_id] = len(pages)

        # Check if scaffold already exists
        scaffold_file = output_dir / f"{subtopic_id}.md"
        if scaffold_file.exists():
            print(f"    ✓ {subtopic_id}: scaffold already exists ({len(pages)} pages)")
            continue

        print(f"    🔨 {subtopic_id}: generating scaffold from {len(pages)} pages...")

        # Concatenate page text with markers
        concatenated_pages = []
        for pdf_name, page_num, page_text in pages:
            concatenated_pages.append(
                f"=== PDF: {pdf_name} | Page: {page_num} ===\n{page_text}"
            )
        concatenated_text = "\n\n".join(concatenated_pages)

        # Limit text length (keep first N chars)
        MAX_CHARS = 30000
        if len(concatenated_text) > MAX_CHARS:
            concatenated_text = (
                concatenated_text[:MAX_CHARS]
                + "\n\n[... content truncated for length ...]"
            )

        # Format must_be_able_to
        must_be_able_to = "\n".join(f"- {item}" for item in spec["must_be_able_to"])

        # Prepare prompt
        prompt = scaffold_template.format(
            subject=spec["subject"],
            title=subtopic_title,
            description=subtopic_desc,
            exam_format=spec["exam_format"],
            must_be_able_to=must_be_able_to,
            concatenated_pages=concatenated_text,
        )

        # Call API with sonar-pro for better quality
        try:
            response = call_perplexity(
                messages=[{"role": "user", "content": prompt}],
                model="sonar-pro",
                temperature=0.2,
            )

            # Save scaffold
            scaffold_file.write_text(response, encoding="utf-8")
            print(f"    ✅ {subtopic_id}: scaffold generated")

        except Exception as e:
            print(f"    ❌ {subtopic_id}: failed to generate scaffold: {e}")

    return stats


# ============================================================================
# PHASE 5: INDEX GENERATION
# ============================================================================


def generate_index(
    spec: Dict[str, Any],
    stats: Dict[str, int],
    pdf_metadata_list: List[Dict[str, Any]],
    output_dir: Path,
) -> None:
    """Generate index.md with overview and links."""
    print("\n  📋 Generating index...")

    index_path = output_dir / "_index.md"

    # Calculate total pages processed
    total_pages = sum(len(pdf["labels"]) for pdf in pdf_metadata_list)

    # Build index content
    lines = [
        f"# {spec['subject']} - Study Scaffolds",
        "",
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "## Exam Format",
        "",
        spec["exam_format"],
        "",
        "## Learning Objectives",
        "",
        "You must be able to:",
        "",
    ]

    for item in spec["must_be_able_to"]:
        lines.append(f"- {item}")

    lines.extend(["", "## Subtopic Scaffolds", ""])

    # Add links to scaffolds
    for subtopic in spec["subtopics"]:
        subtopic_id = subtopic["id"]
        subtopic_title = subtopic["title"]
        page_count = stats.get(subtopic_id, 0)

        scaffold_file = output_dir / f"{subtopic_id}.md"
        if scaffold_file.exists():
            lines.append(
                f"- [{subtopic_title}](./{subtopic_id}.md) ({page_count} pages)"
            )
        else:
            lines.append(f"- {subtopic_title} (no content found)")

    lines.extend(
        [
            "",
            "## Statistics",
            "",
            f"- **Total pages processed:** {total_pages}",
            f"- **Sources used:** {len(pdf_metadata_list)}",
            f"- **Subtopics covered:** {len([s for s in stats.values() if s > 0])}/{len(spec['subtopics'])}",
            "",
        ]
    )

    # Add source breakdown
    lines.extend(["## Source Breakdown", ""])

    for pdf_meta in pdf_metadata_list:
        lines.append(f"- **{pdf_meta['name']}**: {len(pdf_meta['labels'])} pages")

    index_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"  ✅ Index generated: {index_path}")


# ============================================================================
# MAIN ORCHESTRATION
# ============================================================================


def process_subject(subject_dir: Path, cache_dir: Path, output_dir: Path) -> None:
    """Process a single subject directory."""
    spec_file = subject_dir / "spec.yaml"
    sources_dir = subject_dir / "sources"

    if not spec_file.exists():
        print(f"⚠ Skipping {subject_dir.name}: no spec.yaml found")
        return

    if not sources_dir.exists() or not sources_dir.is_dir():
        print(f"⚠ Skipping {subject_dir.name}: no sources/ directory found")
        return

    # Load spec
    with open(spec_file) as f:
        spec = yaml.safe_load(f)

    subject_name = spec["subject"]
    print(f"\n{'=' * 70}")
    print(f"Processing: {subject_name}")
    print(f"{'=' * 70}")

    # Find all PDFs
    pdf_files = list(sources_dir.glob("*.pdf"))
    if not pdf_files:
        print(f"⚠ No PDF files found in {sources_dir}")
        return

    print(f"Found {len(pdf_files)} PDF(s)")

    # Phase 1: Extract all PDFs
    print(f"\n📦 Phase 1: Text Extraction")
    pdf_metadata_list = []

    for pdf_path in pdf_files:
        pdf_hash, total_pages = extract_pdf_text(pdf_path, cache_dir)
        pdf_metadata_list.append(
            {
                "name": pdf_path.name,
                "path": pdf_path,
                "hash": pdf_hash,
                "total_pages": total_pages,
            }
        )

    # Phase 2: Classify pages
    print(f"\n🏷️  Phase 2: Page Classification")
    for pdf_meta in pdf_metadata_list:
        labels = classify_pages(
            pdf_meta["hash"], pdf_meta["name"], pdf_meta["total_pages"], spec, cache_dir
        )
        pdf_meta["labels"] = labels

    # Phase 3: Detect single-topic PDFs
    print(f"\n📊 Phase 3: Single-Topic Detection")
    detect_single_topic_pdfs(pdf_metadata_list, subject_name, cache_dir)

    # Phase 4: Generate scaffolds
    print(f"\n📝 Phase 4: Scaffold Generation")
    subject_output_dir = output_dir / subject_dir.name
    stats = generate_scaffolds(spec, pdf_metadata_list, cache_dir, subject_output_dir)

    # Phase 5: Generate index
    print(f"\n📋 Phase 5: Index Generation")
    generate_index(spec, stats, pdf_metadata_list, subject_output_dir)

    print(f"\n✅ Completed: {subject_name}")


def main():
    """Main entry point."""
    print("=" * 70)
    print("Exam Preparation Script - Study Scaffold Generator")
    print("=" * 70)

    # Load environment variables
    load_env_file()

    # Check for API key
    if not os.environ.get("PERPLEXITY_API_KEY"):
        print("\n❌ ERROR: PERPLEXITY_API_KEY not found!")
        print("   Create a .env file with your API key:")
        print("   echo 'PERPLEXITY_API_KEY=your_key_here' > .env")
        return 1

    # Set up paths
    root_dir = Path(__file__).parent
    subjects_dir = root_dir / "subjects"
    cache_dir = root_dir / "cache"
    output_dir = root_dir / "out"

    # Find all subject directories
    subject_dirs = [d for d in subjects_dir.iterdir() if d.is_dir()]

    if not subject_dirs:
        print(f"\n⚠ No subject directories found in {subjects_dir}")
        return 1

    print(f"\nFound {len(subject_dirs)} subject(s)")

    # Process each subject
    for subject_dir in subject_dirs:
        try:
            process_subject(subject_dir, cache_dir, output_dir)
        except Exception as e:
            print(f"\n❌ Error processing {subject_dir.name}: {e}")
            import traceback

            traceback.print_exc()
            continue

    print("\n" + "=" * 70)
    print("All subjects processed!")
    print("=" * 70)

    return 0


if __name__ == "__main__":
    exit(main())
