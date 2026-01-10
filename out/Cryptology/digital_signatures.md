# Signature schemes

Definition of signatures schemes and of CMA security. The Schnorr signature scheme, you can do many details here, such as the proof that you cannot cheat the underlying interactive game with better than 1/q probability, and the full story on how you derive the signature scheme from the interactive game. Or you can just do the spec of the scheme, giving you time for something else, such as RSA+hash signatures and the proof that secure hash + secure signature scheme is secure. Or you can do the one-time signatures based on hash functions and the proof that they are secure.

## The "Elevator Pitch" (Synthesis)

> **Explain Digital Signature Schemes to a peer in 3 sentences. Focus on WHY we use it, not just how.**


## Core Vocabulary & Syntax (Total Recall)

### Digital Signature System (G, S, V)
[Student must write definition here]

### CMA-secure
[Student must write definition here]

### Full Domain Hash
[Student must write definition here]

### Schnorr signature scheme
[Student must write definition here]

### Interactive game (Schnorr)
[Student must write definition here]

### RSA assumption
[Student must write definition here]


## Logic Flow / Mechanism (Process)

### Schnorr Interactive Game
Derive the steps of the interactive game that proves knowledge of the secret key$a$without revealing it. Provide the verifier's check equation.

1. Signer sends$c = \alpha^r$to verifier, where$r \in \mathbb{Z}_q$random.
2. [____________________]
3. [____________________]
4. Verifier checks$\alpha^z \stackrel{?}{=} c \beta^e \mod p$.

### From Interactive Game to Schnorr Signature Scheme
Fill in the transformation steps using hash function$h$.

1. Replace verifier's random$e$with$e = h(c, m)$.
2. [____________________]
3. [____________________]
4. Verification: Compute$c = \alpha^z \beta^{-e} \mod p$, check$e \stackrel{?}{=} h(c, m)$.

### Full Domain Hash Security Proof (High-Level)
Outline the contradiction proof structure for Theorem 12.2.

1. Assume PPT adversary$A$breaks CMA security with probability$\epsilon$.
2. [____________________]
3. [____________________]
4.$B$'s success probability$\approx \frac{1}{e} \frac{\epsilon}{q_{sig} + 1}$, non-negligible.

## The "Exam Trap" (Distinctions)

**Distinguish between plain RSA signatures and RSA + Full Domain Hash based on: (1) CMA security vulnerability, (2) attack method, (3) role of hash function.**

| Criterion   | Plain RSA                               | RSA + Full Domain Hash                          |
| ----------- | --------------------------------------- | ----------------------------------------------- |
| CMA Attack  | [Student: Describe existential forgery] | [Student: Why attack fails]                     |
| Hash Role   | [Student: None]                         | [Student: Collision intractability implication] |
| Proof Model | [Student: Insecure]                     | [Student: Random oracle + RSA assumption]       |

## Exam Simulation

**Oral Exam Question 1:** "Walk me through the Schnorr interactive game. Prove why a cheater succeeds with probability at most$1/q$. Derive the secret key$a$if the cheater answers two different challenges correctly."

**Oral Exam Question 2:** "Present the Full Domain Hash scheme. Give the security proof intuition under random oracle model and RSA assumption. Compute$B$'s optimal success probability parameter$p$."

**Oral Exam Question 3:** "Explain Theorem 12.4: If$H$is collision intractable and$\Sigma$is secure, then combined$\Sigma'$is secure. Walk through the reduction: given breaker$E'$of$\Sigma'$, how does$E$either forge$\Sigma$or find hash collision?"

## Source Map

- [CryptographyV6.pdf](../../subjects/Cryptology/sources/CryptographyV6.pdf) | Page 147 | Covers: Definition of Digital Signature Schemes
- [CryptographyV6.pdf](../../subjects/Cryptology/sources/CryptographyV6.pdf) | Page 148 | Covers: CMA security definition
- [CryptographyV6.pdf](../../subjects/Cryptology/sources/CryptographyV6.pdf) | Page 149-151 | Covers: RSA + Full Domain Hash scheme and security proof (Theorem 12.2)
- [CryptographyV6.pdf](../../subjects/Cryptology/sources/CryptographyV6.pdf) | Page 152-154 | Covers: Schnorr interactive game, derivation to signature scheme, security lemma
- [CryptographyV6.pdf](../../subjects/Cryptology/sources/CryptographyV6.pdf) | Page 156-157 | Covers: General hash + signature combination (Theorem 12.4)

**Source data missing for: One-time signatures from hash functions and their security proof.**