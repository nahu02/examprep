# Public-key cryptography based on discrete log and LWE

The DL, DH and DDH problems, and how they relate. The El Gamal cryptosystem and proof that it is secure if DDH is hard. Then some example of groups we can use, can be a subgroup of Z_p*, or you can talk about elliptic curves. You can also put less emphasis on El Gamal, for instance skip the example groups and go to LWE instead, define the problem and the cryptosystem and do the proof from the exercise that decryption works under a certain assumption about the noise distribution.

## The "Elevator Pitch" (Synthesis)

> **Explain Public-key Crypto based on Discrete Log to a peer in 3 sentences. Focus on WHY we use it, not just how.**

## Core Vocabulary & Syntax (Total Recall)

### Discrete Log (DL) problem
[Student must write definition here]

### Diffie-Hellman (DH) problem
[Student must write definition here]

### Decisional Diffie-Hellman (DDH) problem
[Student must write definition here]

### GGen
[Student must write definition here]

### El Gamal cryptosystem
[Student must write definition here]

### Generator α
[Student must write definition here]

## Logic Flow / Mechanism (Process)

### El Gamal Key Generation, Encryption, Decryption
1. Run **GGen**(k) to get specification of group **G** and generator **α**.
2. [____________________]
3. [____________________]
4. Public key: specification of **G** and **β**; secret key: **a**.

### El Gamal Encryption of \( m \in G \)
1. Choose **r** at random from \( \mathbb{Z}_t \).
2. [____________________]
3. Ciphertext: \( (\alpha^r, \beta^r m) \).

### El Gamal Decryption of \( (c, d) \)
1. [____________________]
2. Output: \( m \).

### Reduction: CPA Security of El Gamal (Theorem 9.7)
1. Assume adversary **Adv** breaks CPA security of El Gamal with advantage \( \epsilon \).
2. [____________________]
3. [____________________]
4. **B** solves DDH with advantage at least \( \epsilon \), contradiction if DDH hard.

## The "Exam Trap" (Distinctions)

**Distinguish between DL, DH, and DDH problems based on input, output, and hardness implications. Complete the matrix:**

| Problem | Input                                         | Output/Task | Implied by DL?  | Implies DDH?   |
| ------- | --------------------------------------------- | ----------- | --------------- | -------------- |
| **DL**  | \( G, \alpha, \beta \)                        | [Fill in]   | -               | [Fill in]      |
| **DH**  | \( G, \alpha, \alpha^a, \alpha^b \)           | [Fill in]   | Yes (Lemma 9.1) | [Fill in]      |
| **DDH** | \( G, \alpha, \alpha^a, \alpha^b, \alpha^c \) | [Fill in]   | Yes             | No (Lemma 9.2) |

**Why is DDH not hard in \( \mathbb{Z}_p^* \) (Lemma 9.10)? Specify the attack using parities.**

## Exam Simulation

**Oral Exam Question 1:** "Present the El Gamal cryptosystem: specify key generation, encryption, decryption algorithms, and verify decryption works by direct computation."

**Oral Exam Question 2:** "Prove Theorem 9.7: If DDH is hard w.r.t. GGen, then El Gamal is CPA secure. Construct the reduction algorithm B using adversary Adv as a subroutine."

**Oral Exam Question 3:** "Explain why \( \mathbb{Z}_p^* \) cannot yield CPA-secure El Gamal (Lemma 9.10). Then describe prime order subgroups of \( \mathbb{Z}_p^* \) for safe primes and the encoding from \( \mathbb{Z}_q \) to G."

## Source Map
- [CryptographyV6.pdf](../../subjects/Cryptology/sources/CryptographyV6.pdf) | Page 115-117 | Covers: DL, DH, DDH problems and definitions
- [CryptographyV6.pdf](../../subjects/Cryptology/sources/CryptographyV6.pdf) | Page 117 | Covers: El Gamal cryptosystem (general version), decryption verification (Lemma 9.6)
- [CryptographyV6.pdf](../../subjects/Cryptology/sources/CryptographyV6.pdf) | Page 116 | Covers: Theorem 9.7 (CPA security if DDH hard), Exercise 9.1 (proof sketch)
- [CryptographyV6.pdf](../../subjects/Cryptology/sources/CryptographyV6.pdf) | Page 120 | Covers: Why DDH not hard in \( \mathbb{Z}_p^* \) (Lemma 9.10), safe primes, prime order subgroups
- **Source data missing for LWE problem and cryptosystem** (no details in provided excerpts)