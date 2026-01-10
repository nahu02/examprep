# Symmetric Authentication and Hash Functions

Definition of collision-intractable hash functions. Then a selection of: construction from discrete log, proof that collision-intractable implies one-way, construction and proof that we can get any size input from fixed size input. Finally, MAC schemes, definition of CMA security, CBCMAC and EMAC security result for EMAC. Maybe a brief mention of HMAC.

## The "Elevator Pitch" (Synthesis)

**Prompt:** Explain the core purpose of symmetric authentication systems and hash functions in 3 sentences. Focus on the *problem they solve* and *why collision resistance matters more than preimage resistance*.

> [Write your answer here]

---

## Core Vocabulary & Syntax (Total Recall)

Define each term precisely using the source material. Include the mathematical notation or context where applicable.

### Collision-intractable hash function
[Your definition]

### Second preimage attack
[Your definition]

### Collision attack
[Your definition]

### Message digest / fingerprint
[Your definition]

### Domain extension
[Your definition]

### Merkle-Damgård construction
[Your definition]

### Suffix-free encoding
[Your definition]

### Birthday paradox (in the context of hash functions)
[Your definition]

### Random oracle model
[Your definition]

---

## Logic Flow / Mechanism (Process)

### A. Discrete Log-Based Hash Function Construction

You are given the discrete log hash function: $h(m_1, m_2) = \alpha^{m_1}\beta^{m_2} \bmod p$

**Task:** Reconstruct the proof that if discrete log is hard, then $h$ is collision-intractable.

1. Assume an adversary finds a collision: $(m_1, m_2) \neq (m_1', m_2')$ with $h(m_1, m_2) = h(m_1', m_2')$.
2. [____________________] (What equation do you now have?)
3. [____________________] (What case analysis must you perform?)
4. [____________________] (How do you isolate $\alpha$ in terms of $\beta$?)
5. Conclude: You have computed the discrete logarithm of $\alpha$ base $\beta$, contradicting the hardness assumption.

---

### B. Merkle-Damgård Domain Extension (Case: $m - k > 1$)

You have a collision-intractable function $f: \{0,1\}^m \to \{0,1\}^k$ where $m > k$.

**Task:** Fill in the missing steps of the construction that produces $h: \{0,1\}^* \to \{0,1\}^k$.

1. Set $v = m - k - 1$. Split input $x$ into $v$-bit blocks: $x_1, \ldots, x_n$.
2. [____________________] (What is the padding step?)
3. Define the starting state: $z_1 = 0^k $ 1 $ x_1$. For $i = 2, \ldots, n+1$, define [____________________].
4. [____________________] (What is the final output?)
5. **Proof sketch:** If $h(x) = h(x')$ for $x \neq x'$, show that you can work backwards through the sequences $z_i$ and $z_i'$ to find a collision for $f$. Why is the single bit in position $k+1$ critical?

---

### C. Proving Collision-Intractable Implies One-Way (Lemma 11.2)

**Task:** Complete the logical chain.

1. Assume you have an algorithm $A$ that inverts $h$ with probability $\epsilon$ in time $t$.
2. [____________________] (What is the collision-finding algorithm?)
3. [____________________] (Define "only child" and compute the probability that a random $m$ is an only child.)
4. [____________________] (Why does $P[C|G] \geq 1/2$ when $m$ is not an only child?)
5. Conclude: $P[\text{collision}] \geq (\epsilon - 2^{-k})/2$, which is non-negligible if $\epsilon$ is non-negligible.

---

## The "Exam Trap" (Distinctions)

### Collision Resistance vs. Preimage Resistance

**Instruction:** Distinguish between these two security properties using the criteria below.

| Criterion                                     | Collision Resistance           | Preimage Resistance |
| --------------------------------------------- | ------------------------------ | ------------------- |
| **Definition**                                | [Your answer]                  | [Your answer]       |
| **Adversary's goal**                          | [Your answer]                  | [Your answer]       |
| **Which is stronger?**                        | [Your answer]                  | [Your answer]       |
| **Why is collision resistance the standard?** | [Your answer]                  | [Your answer]       |
| **Relationship**                              | If you can do X, can you do Y? | [Your answer]       |

---

### Hash Functions in Theory vs. Practice

**Instruction:** Explain why the theoretical definition of collision-intractable hash functions (Definition 11.1) requires a *generator* $H$ rather than a single fixed function. Then contrast this with how SHA-3 is used in practice.

> [Write your answer here]

---

## Exam Simulation

### Question 1 (Presentation + Follow-up)

**Scenario:** You randomly select "Hash Functions" as your oral exam topic. You have 18 minutes to present.

**Prompt:** 
- **Part A (Presentation):** Walk through the discrete log-based hash function construction. Explain why the collision-intractability of $h(m_1, m_2) = \alpha^{m_1}\beta^{m_2} \bmod p$ follows from the hardness of discrete log. Include the proof strategy.
- **Part B (Follow-up Question):** "Your construction only handles 2(k-1)-bit inputs. How do you extend this to arbitrary-length inputs, and why is the single bit in the Merkle-Damgård construction necessary?"

---

### Question 2 (Proof Reconstruction)

**Prompt:** 
State and prove **Lemma 11.2**: "If a hash function $h: \{0,1\}^{2k} \to \{0,1\}^k$ can be inverted with probability $\epsilon$ in time $t$, then a collision can be found in time $t$ plus one evaluation of $h$ with probability at least $\epsilon/2 - 2^{-k-1}$."

Your proof should:
1. Describe the collision-finding algorithm.
2. Define the event "only child" and compute its probability.
3. Explain why $P[C|G] \geq 1/2$ (where $C$ is collision and $G$ is the event that $m$ is not an only child and $A$ succeeds).
4. Conclude with the final probability bound.

---

### Question 3 (Conceptual Depth)

**Prompt:** 
"The random oracle model assumes the hash function behaves like a random function. Explain:
1. What is a random oracle, and how does it differ from a concrete hash function like SHA-256?
2. Why does the birthday paradox (Theorem 11.4) imply that $k \geq 160$ bits?
3. What does it mean for an application to be 'secure in the random oracle model,' and what are its limitations?"

---

## Source Map

| Source             | Location      | Coverage                                                                    |
| ------------------ | ------------- | --------------------------------------------------------------------------- |
| CryptographyV6.pdf | Page 134      | Definition 11.1: Collision-intractable hash functions                       |
| CryptographyV6.pdf | Page 135      | Section 11.2.1: Discrete log and RSA-based constructions                    |
| CryptographyV6.pdf | Page 135      | Section 11.2.2: Lemma 11.2 (collision-intractable implies one-way)          |
| CryptographyV6.pdf | Pages 136–138 | Section 11.2.3: Merkle-Damgård domain extension (Theorem 11.3)              |
| CryptographyV6.pdf | Pages 138–139 | Section 11.2.4: Hash functions in practice (SHA-1, SHA-3, birthday paradox) |
| CryptographyV6.pdf | Pages 139–140 | Section 11.2.5: Random oracle model                                         |

---

## Critical Gaps & Missing Content

**Source data incomplete for:**
- Detailed proofs of RSA-based hash functions (Exercise 11.1 is stated but not fully worked).
- Formal security definitions for MAC schemes (Section 11.3 is referenced but not included in the provided excerpt).
- CBCMAC and EMAC constructions and their security proofs (mentioned in learning objectives but not in provided text).
- HMAC construction and security analysis (mentioned in learning objectives but not in provided text).

**Recommendation:** Consult the full CryptographyV6.pdf for Sections 11.3 and 11.4 to complete your preparation on MAC schemes.