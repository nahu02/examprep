# Symmetric (secret-key) cryptography

What a crypto-system is (the three algorithms) You can describe DES or AES - but you can also just give a high-level description of what a block cipher is. Definitions of PRF and CPA security. Specification of CBC or CTR modes (or both), proofs of CPA security for CBC or CTR mode (or both). Perhaps a brief talk about stream ciphers and how to make one from a block cipher.

## The "Elevator Pitch" (Synthesis)

> **Explain Symmetric (secret-key) Crypto to a peer in 3 sentences. Focus on WHY we use it, not just how.**


## Core Vocabulary & Syntax (Total Recall)

### Cryptosystem

[Student must write definition here]

### G (Key Generation)

[Student must write definition here]

### E (Encryption)

[Student must write definition here]

### D (Decryption)

[Student must write definition here]

### Key space K

[Student must write definition here]

### Plaintext space P

[Student must write definition here]

### Ciphertext space C

[Student must write definition here]

### Block cipher

[Student must write definition here]


## Logic Flow / Mechanism (Process)

**Construct a symmetric cryptosystem (G, E, D). Fill in the requirements and correctness condition.**

1. Define finite sets: **K**, **P**, **C**.
2. [____________________]
3. [____________________]
4. Require: For any $ K $ from **G**, and any $ x \in P $, $ x = D_K(E_K(x)) $.

**Encrypt a message with the Shift Cipher. Derive the steps.**

1. Choose $ K $ uniformly from $ K = \mathbb{Z}_n $.
2. [____________________]
3. [____________________]

## The "Exam Trap" (Distinctions)

**Distinguish between attack models based on oracle access. Complete the matrix:**

| Attack Type                | Oracle Input    | Oracle Output   | Adversary Knowledge |
| -------------------------- | --------------- | --------------- | ------------------- |
| **Ciphertext Only**        | [Student fills] | [Student fills] | [Student fills]     |
| **Known Plaintext**        | [Student fills] | [Student fills] | [Student fills]     |
| **Chosen Plaintext (CPA)** | [Student fills] | [Student fills] | [Student fills]     |
| **Chosen Ciphertext**      | [Student fills] | [Student fills] | [Student fills]     |

## Exam Simulation

**Oral Exam Question 1:** "Walk me through the definition of a symmetric cryptosystem, including the three algorithms and their inputs/outputs. Specify the sets involved and the correctness requirement."

**Oral Exam Question 2:** "Describe DES and AES as modern symmetric cryptosystems. What historical context led to DES, and why was a successor like AES needed? Reference their structure (e.g., Feistel for DES)."

**Oral Exam Question 3:** "Source data missing for PRF definition, CPA security definitions, CBC/CTR mode specifications, and their CPA security proofs. Explain from course material: Define PRF and CPA security. Specify CBC or CTR mode and prove its CPA security assuming a secure block cipher."

## Source Map

- [CryptographyV6.pdf](../../subjects/Cryptology/sources/CryptographyV6.pdf) | Page 27-28 | Covers: Symmetric cryptosystem definition (G, E, D), sets K/P/C, correctness.
- [CryptographyV6.pdf](../../subjects/Cryptology/sources/CryptographyV6.pdf) | Page 28 | Covers: Shift Cipher example.
- [CryptographyV6.pdf](../../subjects/Cryptology/sources/CryptographyV6.pdf) | Page 29 | Covers: Attack models (ciphertext-only, known/chosen plaintext/ciphertext).
- [CryptographyV6.pdf](../../subjects/Cryptology/sources/CryptographyV6.pdf) | Page 60-61 | Covers: DES blockcipher, Feistel structure, history.
- [CryptographyV6.pdf](../../subjects/Cryptology/sources/CryptographyV6.pdf) | Page 58,63 | Covers: DES and AES blockciphers (high-level).