# Exam Preparation Script

AI-powered study scaffold generator that transforms PDF course materials into structured study guides using the Perplexity API.

## Overview

This tool helps students create **study scaffolds** (not complete notes) from academic PDFs. It:

1. **Extracts** text from PDFs page-by-page
2. **Classifies** each page into predefined subtopics
3. **Generates** Markdown study frameworks with blanks to fill
4. **Caches** aggressively to minimize API costs on reruns
5. **Detects** single-topic PDFs for optimization

The output is a set of Markdown files with structured study guides that prompt you to fill in gaps from the source material—encouraging active learning rather than passive reading.

## Features

✅ **Smart Caching**: Only processes new/changed PDFs  
✅ **Cost-Effective**: Uses `sonar` for classification, `sonar-pro` for scaffolds  
✅ **Page-Level Precision**: Each page classified to specific subtopics  
✅ **Source Citations**: Every scaffold cites exact pages to read  
✅ **Structured Output**: Consistent Markdown format for easy review  
✅ **Single-Topic Detection**: Optimizes for textbooks vs. slide decks  

## Project Structure

```
examprep/
├── exam_prep.py          # Main script
├── requirements.txt      # Python dependencies
├── .env                  # API key (create from .env.example)
├── .env.example          # Template for environment variables
├── README.md             # This file
│
├── prompts/              # AI prompt templates
│   ├── classify_page.txt
│   └── generate_scaffold.txt
│
├── subjects/             # Your course materials
│   └── <subject_name>/
│       ├── spec.yaml     # Subject configuration
│       └── sources/      # PDF files go here
│
├── cache/                # Intermediate results (gitignored)
│   ├── extracted/        # Page-by-page text extraction
│   │   └── <pdf_hash>/
│   │       ├── metadata.json
│   │       └── page_NNN.txt
│   └── labels/           # Page classification results
│       ├── <subject>.jsonl
│       └── <pdf_hash>.jsonl
│
└── out/                  # Generated study scaffolds (gitignored)
    └── <subject_name>/
        ├── index.md      # Overview with links
        └── <subtopic_id>.md
```

## Installation

### Prerequisites

- Python 3.10 or higher
- Perplexity API key ([get one here](https://www.perplexity.ai/settings/api))

### Setup

1. **Clone or download this project**

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API key**:
   ```bash
   cp .env.example .env
   # Edit .env and add your Perplexity API key
   ```

4. **Add your course materials**:
   - Create a subject directory: `subjects/YourSubject/`
   - Add a `spec.yaml` file (see format below)
   - Place PDFs in `subjects/YourSubject/sources/`

## spec.yaml Format

Create a `spec.yaml` file for each subject:

```yaml
subject: "Your Subject Name"
exam_format: "Description of exam format (e.g., '2-hour written exam with MCQs and essays')"

must_be_able_to:
  - "Learning objective 1"
  - "Learning objective 2"
  - "Learning objective 3"

subtopics:
  - id: unique_id_1
    title: "Subtopic Title"
    description: "Brief description of what this covers"
  
  - id: unique_id_2
    title: "Another Subtopic"
    description: "Another description"
```

**Example**: See `subjects/Human-Computer Interaction/spec.yaml`

## Usage

### Run the script:

```bash
python exam_prep.py
```

The script will:
1. Find all subjects with `spec.yaml` files
2. Extract text from PDFs (cached after first run)
3. Classify pages into subtopics using AI
4. Generate study scaffolds for each subtopic
5. Create an index file with links

### On subsequent runs:

- Already-extracted PDFs are skipped (unless file changed)
- Already-classified pages are skipped
- Already-generated scaffolds are skipped

To regenerate scaffolds, delete the files in `out/<subject>/`

## Output Format

Each subtopic scaffold includes:

- **Overview**: 2-3 sentence summary
- **Key Concepts to Master**: Bullet points with blanks to fill
- **Definitions**: Terms with blank spaces for you to define
- **Important Distinctions**: Comparisons between similar concepts
- **Example to Reproduce**: Prompts to work through examples
- **Likely Exam Questions**: Practice questions based on exam format
- **Sources to Read**: Table of PDFs and pages to study

Example scaffold structure:

```markdown
# Activity Theory

## Overview
[Brief summary of the subtopic]

## Key Concepts to Master
- **______** is the hierarchical structure consisting of...
- The process of ______ refers to...

## Definitions (Fill These In)
- **Mediation**: ____________
- **Internalization**: ____________

## Sources to Read
| PDF | Pages | Why Read |
|-----|-------|----------|
| textbook.pdf | 45-52 | Core theory explanation |
```

## Cost Management

The script is designed to minimize API costs:

- **Classification**: Uses `sonar` model (fast, cheap)
- **Scaffolds**: Uses `sonar-pro` model (better quality)
- **Caching**: Never reclassifies or regenerates existing content
- **Truncation**: Long pages are truncated to avoid token limits

**Estimated costs** (as of Dec 2024):
- Classification: ~$0.001-0.002 per page
- Scaffold generation: ~$0.05-0.10 per subtopic
- For a 200-page course with 10 subtopics: ~$1-2 total

## Troubleshooting

### "PERPLEXITY_API_KEY not found"
Create a `.env` file with your API key (see Installation step 3)

### "PyMuPDF not installed"
Run: `pip install pymupdf`

### "No PDF files found"
Ensure PDFs are in `subjects/<YourSubject>/sources/` directory

### API rate limiting
The script includes automatic retry logic. If you hit rate limits, results are cached so you can resume.

### Empty or incorrect classifications
- Check that PDF text extraction worked (inspect `cache/extracted/`)
- Verify your subtopic descriptions are clear and distinct
- Some pages (covers, blank pages) will be marked IRRELEVANT—this is expected

## Advanced Usage

### Custom Prompts

Edit prompt templates in `prompts/`:
- `classify_page.txt`: Controls page classification behavior
- `generate_scaffold.txt`: Controls scaffold structure and content

Use `{variable}` placeholders that will be filled by the script.

### Processing Specific Subjects

The script processes all subjects in `subjects/`. To process only one:
1. Temporarily move other subject directories elsewhere, or
2. Modify the script's `main()` function to filter subjects

### Clearing Cache

To force re-processing:
- Delete `cache/extracted/<pdf_hash>/` to re-extract a PDF
- Delete `cache/labels/<pdf_hash>.jsonl` to re-classify pages
- Delete `out/<subject>/<subtopic>.md` to regenerate a scaffold

## How It Works

### Phase 1: Text Extraction
- Uses PyMuPDF (fitz) to extract text page-by-page
- Calculates SHA256 hash of PDF for cache invalidation
- Stores each page as `page_NNN.txt`
- Stores metadata (filename, page count, extraction time)

### Phase 2: Page Classification
- Loads each page's text from cache
- Sends to Perplexity `sonar` model with classification prompt
- Receives JSON response: `{rationale, label, confidence}`
- Appends to JSONL file (one line per page)
- Skips pages already in JSONL (resumable)

### Phase 3: Single-Topic Detection
- Analyzes label distribution per PDF
- If one subtopic covers ≥85% of pages, marks as "single-topic"
- Stores in `cache/labels/<subject>.jsonl`
- (Currently informational; future: could optimize scaffold generation)

### Phase 4: Scaffold Generation
- Groups all pages by subtopic across all PDFs
- Concatenates page text with clear markers
- Sends to Perplexity `sonar-pro` model with scaffold prompt
- Saves Markdown output to `out/<subject>/<subtopic_id>.md`

### Phase 5: Index Generation
- Creates `index.md` with:
  - Subject metadata and learning objectives
  - Links to all subtopic scaffolds
  - Statistics (pages processed, sources used)
  - Source breakdown

## API Details

### Models Used

- **sonar**: Fast, cost-effective, good for classification
- **sonar-pro**: Higher quality, better for long-context generation

### API Endpoint

```
POST https://api.perplexity.ai/chat/completions
```

### Request Format

```python
{
  "model": "sonar" or "sonar-pro",
  "messages": [
    {"role": "user", "content": "your prompt"}
  ],
  "temperature": 0.0,  # deterministic
  "response_format": {"type": "json_object"}  # for classification
}
```

### Error Handling

- Automatic retry on API errors (1 retry by default)
- Failed classifications marked as IRRELEVANT
- Failed scaffolds logged but don't stop processing
- All errors printed with context

## Contributing

To extend this script:

1. **Add new prompt templates**: Create `.txt` files in `prompts/`
2. **Modify classification logic**: Edit `classify_pages()` function
3. **Change scaffold structure**: Edit `prompts/generate_scaffold.txt`
4. **Add post-processing**: Add functions after Phase 5

## License

This project is provided as-is for educational purposes.

## Support

For issues or questions:
1. Check the Troubleshooting section above
2. Review Perplexity API docs: https://docs.perplexity.ai/
3. Inspect cache files to debug processing

## Acknowledgments

- **Perplexity API**: For AI-powered classification and generation
- **PyMuPDF**: For reliable PDF text extraction
- **You**: For using this to study smarter, not harder! 📚✨
