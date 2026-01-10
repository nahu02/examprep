# Public-key cryptography from Factoring

What a public-key cryptosystem is. Basic spec of RSA, maybe proof that decryption works. Then some selection of the following: How to make RSA be CPA secure (the PCRSA scheme, and the result that computing the least significant bit is as hard as inverting RSA). How to generate keys and Miller-Rabin primality testing, how to get CCA security: OAEP and the intuition on why it works.

## The "Elevator Pitch" (Synthesis)

> **Explain Public-key Crypto based on Factoring to a peer in 3 sentences. Focus on WHY we use it, not just how.**


## Core Vocabulary & Syntax (Total Recall)

### Public-key cryptosystem

[Student must write definition here]

### Trapdoor one-way function

[Student must write definition here]

### RSA

[Student must write definition here]

### Chinese Remainder Theorem

[Student must write definition here]

### Miller-Rabin test

[Student must write definition here]

### $\phi(n)$

[Student must write definition here]

### $f_n$

[Student must write definition here]


## Logic Flow / Mechanism (Process)

### RSA Key Generation
1. Choose random k/2-bit primes $p, q$ and set $n = pq$.
2. [____________________]
3. [____________________]
4. Output $pk = (n, e)$, $sk = (n, d)$.

### RSA Encryption/Decryption Correctness Proof
1. Compute $D(n,d)(E(n,e)(x)) = (x^e \mod n)^d \mod n = x^{ed} \mod n$.
2. [____________________]
3. [____________________]
4. Conclude $= x$.

### Miller-Rabin Primality Test
1. On input odd $x$, compute $a, b$ such that $x-1 = 2^a b$ where $b$ is odd.
2. [____________________]
3. [____________________]
4. Accept if any $w^{2^i b} \mod x = -1$ or $w^b \mod x = 1$, else reject.

### Random Prime Generation
1. Select uniform random k-bit $x$ with $2^k \leq x < 2^{k+1}$.
2. [____________________]
3. Repeat until accept.

## The "Exam Trap" (Distinctions)

**Distinguish between $f_n$ and $f_n^{-1}$ in the Chinese Remainder Theorem based on input domain, output domain, and computation of $a_p, a_q$.**

| Aspect                    | $f_n$               | $f_n^{-1}$          |
| ------------------------- | ------------------- | ------------------- |
| **Input**                 | [Student must fill] | [Student must fill] |
| **Output**                | [Student must fill] | [Student must fill] |
| **Key Computation**       | [Student must fill] | [Student must fill] |
| **Homomorphism Property** | [Student must fill] | [Student must fill] |

## Exam Simulation

1. **Oral Presentation Prompt:** "Walk me through the full specification of a public-key cryptosystem, including the roles of G, E, D and the correctness requirement. Present for up to 18 minutes, then field questions."

2. **Oral Proof Prompt:** "Prove that RSA decryption works for $x \in \mathbb{Z}_n^*$. Start from $D(E(x))$ and use group properties and CRT intuition. Be ready for follow-ups on $\phi(n)$."

3. **Oral Security/Implementation Prompt:** "Explain how to generate RSA keys, including prime generation via Miller-Rabin. Detail the test steps, error analysis for composites, and why repeated iterations suffice in practice."

## Source Map
- [CryptographyV6.pdf](../../subjects/Cryptology/sources/CryptographyV6.pdf) | Page 22-24 | Covers: Chinese Remainder Theorem (special/general case), group exponent arithmetic modulo $|G|$.
- [CryptographyV6.pdf](../../subjects/Cryptology/sources/CryptographyV6.pdf) | Page 86-94 | Covers: Public-key cryptosystem definition, RSA spec/keygen/encryption/decryption, decryption proof, modular exponentiation, Extended Euclidean, Miller-Rabin test/probabilities, prime generation.
- **Source data missing for:** PCRSA scheme, CPA security (LSB hardness), OAEP/CCA intuition.