# Public-key cryptography based on discrete log and LWE

The DL, DH and DDH problems, and how they relate.
The El Gamal cryptosystem and proof that it is secure if DDH is hard.
Then some example of groups we can use, can be a subgroup of Z_p*, or you can talk about elliptic curves.
You can also put less emphasis on El Gamal, for instance skip the example groups and go to LWE instead, define the problem and the cryptosystem and do the proof from the exercise that decryption works under a certain assumption about the noise distribution.

## The "Elevator Pitch" (Synthesis)

> **Explain Public-key Crypto based on Discrete Log to a peer in 3 sentences. Focus on WHY we use it, not just how.**

## Core Vocabulary & Syntax (Total Recall)

### Discrete Log (DL) problem
> Given a group $G$, generator $\alpha$, and element $\beta \in G$, find integer $a$, such that $\alpha^a = \beta$.

> This is the "reverse" of modular exponentiation. While computing $\alpha^a \bmod p$ is efficient even for large $a$, finding $a$ from $\alpha^a \bmod p$ seems to be computationally infeasible when $p$ is a sufficiently large prime (at least 2048 bits).
> This asymmetry - easy to compute forward, hard to reverse - makes it a one-way function suitable for cryptography.


> The DL problem is in many groups notoriously hard, for instance in $Z_p^*$.

### Diffie-Hellman (DH) problem
> Given a group $G$, generator $\alpha$, and $\alpha^a, \alpha^b$, where $a, b$ are randomly and independently chosen from $\Z_t$, compute $\alpha^{ab}$.

> Notice that you're **not** asked to find $a$ or $b$—just the shared secret $g^{ab}$.
> However, if we could find $a$ from $\alpha^a$, we could solve DH by a single exponentiation, so
> *The DH problem is no harder than the DL problem.*
 
### Decisional Diffie-Hellman (DDH) problem
> The DH problem has a peculiar property, namely if I give you a group element and I claim it solves a DH instance, it is not clear that you can verify that the solution is correct, at least not unless you can solve DL.
> You would need to decide if, for given $\alpha^a, \alpha^b, \alpha^c$, it holds that $c = ab \bmod t$.
> This seems to require that you solve DL (although it is NOT clear that this would be necessary).

> The idea behind the DDH is that you get an instance of the DH problem, plus an extra group element which is either a correct DH solution, or is a random element.
> You are then supposed to guess which case you are in.

> Formally:<br/>
> Given a group $G$, generator $\alpha$, and $\alpha^a, \alpha^b, \alpha^c$,
> where $a, b$ are randomly and independently chosen from $\Z_t$;
> and where $c$ is chosen either as $c = ab$, or uniformly random from $\Z_t$.
> Now guess which of the two cases we are in.

> Clearly, if you could solve DH, then you could solve DDH, by computing $\alpha^{ab}$ and comparing this to $\alpha^c$.
> Therefore, DDH is no harder than DH


### Diffie-Hellman key exchange protocol (DHE)
> In 1977, Diffie and Hellman suggested to use the DH problem as a basis for establishing a shared secret two parties $A$ and $B$ that share no secret key in advance.
> The method for this is very simple, assuming that we already agreed (in public) on a group $G$ and a generator $\alpha$
> 1. $A$ chooses $S_A$ at random in $\Z_t$, $B$ chooses $S_B$ at random in $\Z_t$.
> 2. $A$ sends $y_A = \alpha^{S_A}$ to $B$, $B$ sends $y_B = \alpha^{S_B}$ to $A$.
> 3. $A$ computes $y_B^{S_A}$ and $B$ computes $y_A^{S_B}$

> $A$ and $B$ compute the same value in the last step, since $y_B^{S_A} = y_A^{S_B} = \alpha^{S_A S_B}$.
> An adversary observing the communication would need to solve an instance of the DH problem to find the shared value.

> This (or its elliptic curve version) is still often used: in TLS 1.3 handshakes, the use of (EC)DHE is mandatory, where a server and a client use it to agree on the key they would use for their further AES or 

> Later on El Gamal suggested a way to turn this idea into a regular public key cryptosystem.
> What we do is essentially to consider $A$'s first message in the above as a part of his public key, then $B$'s part of the protocol can be modified to be an encryption:


### El Gamal cryptosystem and proof it is secure (provided DDH is)
> To turn the DH key exchange protocol into a public-key crypto system,
> what we do is essentially to consider $A$'s first message as a part of his public key,
> then $B$'s part of the protocol can be modified to be an encryption.
>
> **Key generation**
> On group $G$ and generator $\alpha$ choose $a$ at random from $\Z_t$. 
> Then the public key is the specification of $G$ and $\beta = \alpha^a$, while the secret key is $a$.
> The plaintext space is $G$ while the ciphertext space is $G \times G$.<br/>
> **Encryption**
> To encrypt $m \in G$, we choose $r$ at random from $\Z_t$, and the ciphertext is $(\alpha^r, \beta^r m)$.<br/> 
> **Decryption** To decrypt ciphertext $(c, d)$, compute $c^{-a} d$.

> To see that decryption works, simply plug in $(\alpha^r, \beta^r m)$ for $(c, d)$ in the decryption algorithm:
> $$c^{-a} d = (\alpha^r)^{-a} \beta^r m = \alpha^{-ra} (\alpha^a)^r m = \alpha^{-ra} \alpha^{ra} m = m$$

> The problem of decrypting an El Gamal ciphertext (without the secret key) is equivalent to solving the DH problem.

> If the DDH problem is hard, then the El Gamal cryptosystem is CPA secure.

### LWE. LWE based cryptosystem and proof decryption works (under certain noise distribution assumption) 
> The LWE problem is defined over a finite field $F_q$ where $q$ is a prime, and all computations in the following will be modulo $q$, even if we do not say so explicitly.
> A secret vector $\vec{s} \in F_q^n$ will be involved.

> The problem is:
> You are given $\{\vec{a_i} \in F_q^n\}_{i=1}^m$ (columns of $n\times m$ mx) and $\{\vec{a_i} \cdot \vec{s} + e_i\}_{i=1}^m$ where the $e_i$'s are random but numerically “small”.
> The goal is now to find $\vec{s}$.

> The $e_i$'s being random and numerically "small" can mean different things, but always means that they are much smaller than $q$.
> For instance, $e_i$ can be chosen uniformly in the interval $[-\sqrt{q} .. \sqrt{q}]$.
> Or it can be chosen using a discrete Gaussian distribution with mean 0 and standard deviation much smaller than $q$.
> It turns out that the exact details of this are not very important as to how hard the problem is.<br/>
> It is fine if we simply assume that the $e_i$'s are chosen with a distribution $D_e$ with the following important property:
> even if you sample $m$ values distributed according to $D_e$, take numeric value and sum them, the result will be smaller than $q/4$ with overwhelming probability.

> The motivation for the name of the problem is that the adversary gets some partial information on $\vec{s}$
> and tries to learn it from this information, but the problem is non-trivial because the "errors" $e_i$ are added in.
> Of course, without the errors the problem would be easy once $m > n$ since then one just solves the linear equations to get $\vec{s}$.

> There is also a decision version of LWE (think DDH for DH):
> you are given random ${\vec{a_i} \in F_q^n}{i=1}^m$
> and then either ${\vec{a_i} \cdot \vec{s} + e_i}{i=1}^m$ or ${u_i}_{i=1}^m$ where the $u_i$ are uniformly random.
> The goal is now to decide which case you are in.

> Decision LWE (DLWE) is hard if any probabilistic polynomial-time (PPT) algorithm can distinguish the two cases with only negligible advantage in $n$ (where $m$ is polynomial in $n$).

> To make a secret-key cryptosystem from LWE:<br/>
> **Key Generation**
> Secret key: random vector $\vec{s} \in F_q^n$.
> Public key: $\{c_i\}_{i=1}^m$, where $c_i = (\vec{a_i}, \vec{a_i} \cdot \vec{s} + e_i)$,
> where $\vec{a_i}$ are uniformly random and the $e_i$ are chosen according to $D_e$.<br/>
> **Encryption** Message is a bit $w$. Choose random bits $b_1, ..., b_m$ and then the ciphertext is $\sum_{i=1}^m b_i c_i + (0, \lfloor q/2 \rfloor w)$<br/>
> **Decryption** To decrypt $(\mathbf{u}, v)$, compute $v - \vec{s} \cdot \mathbf{u}$, and output 0 if this value is closer to 0 than it is to $\lfloor q/2 \rfloor$. Output 1 otherwise.

#### Correctness of LWE Decryption

Any given $c_i$ looks like $c_i = (\vec{a_i}, \vec{a_i} \cdot \vec{s} + e_i)$.
We can also think of these as rows to a matrix and a vector describing a system of linear equations.

(Since $b_i \in \{0, 1\}$, the sum $\sum_{i=1}^{m} b_i c_i$ is really just selecting a subset of the public key components $c_i$ and adding them together.
Knowing that all $c_i$'s solve to $0$, all items of this subset and their sum will also solve to $0$.)

The full cyphertext is:
$$
y = \left( \vec{u}, v \right) = \sum_{i=1}^{m} b_i \vec{a_i}, \sum_{i=1}^{m} b_i \left (\vec{a_i} \cdot \vec{s} + e_i \right ) + \left\lceil\frac{q}{2}\right\rceil w
$$

When decrypting, we compute:
$$
d := v - \vec{u} \cdot \vec{s} = \\
\left( \sum_{i=1}^{m} b_i \left (\vec{a_i} \cdot \vec{s} + e_i  \right ) + \left(\left\lceil\frac{q}{2}\right\rceil w \right) \right) - \left( \sum_{i=1}^{m} b_i \vec{a_i} \right) \cdot \vec{s} = \\
\sum_{i=1}^{m} b_i \left (\vec{a_i} \cdot \vec{s} + e_i - \vec{a_i} \cdot \vec{s} \right ) + \left\lceil\frac{q}{2}\right\rceil w = \\
\sum_{i=1}^{m} b_i e_i + \left\lceil\frac{q}{2}\right\rceil w
$$

We know that $\sum_{i=1}^{m} |e_i| < \frac{q}{4}-1$, and because $b_i \in \{0,1\}$
$$
\left| \sum_{i=1}^{m} b_i e_i \right| \leq \sum_{i=1}^{m} |e_i| < \frac{q}{4}-1
$$

For $w = 0$ we expect $d$ to be closer to $0$ than to $\frac{q}{2}$, meaning $|d| < \frac{q}{4}$.
Indeed, we have:
$$
|d| = \left| \sum_{i=1}^{m} b_i e_i + \left\lceil\frac{q}{2}\right\rceil \cdot 0 \right| < \frac{q}{4}-1 < \frac{q}{4}
$$

For $w = 1$ we expect $d$ to be closer to $\frac{q}{2}$ than to $0$, meaning $|d - \frac{q}{2}| < \frac{q}{4}$.
We have:
$$
|d - \frac{q}{2}| = \left| \sum_{i=1}^{m} b_i e_i + \left\lceil\frac{q}{2}\right\rceil \cdot 1 - \frac{q}{2} \right| < \frac{q}{4} - 1 + 0.5 = \frac{q}{4}
$$

## Logic Flow / Mechanism (Process)

### El Gamal Key Generation, Encryption, Decryption
1. Run **GGen**(k) to get specification of group **G** and generator **α**.
2. [____________________]
3. [____________________]
4. Public key: specification of **G** and **β**; secret key: **a**.

### El Gamal Encryption of \( m \in G \)
1. Choose **r** at random from \( \Z_t \).
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

**Why is DDH not hard in \( \Z_p^* \) (Lemma 9.10)? Specify the attack using parities.**

## Exam Simulation

**Oral Exam Question 1:** "Present the El Gamal cryptosystem: specify key generation, encryption, decryption algorithms, and verify decryption works by direct computation."

**Oral Exam Question 2:** "Prove Theorem 9.7: If DDH is hard w.r.t. GGen, then El Gamal is CPA secure. Construct the reduction algorithm B using adversary Adv as a subroutine."

**Oral Exam Question 3:** "Explain why \( \Z_p^* \) cannot yield CPA-secure El Gamal (Lemma 9.10). Then describe prime order subgroups of \( \Z_p^* \) for safe primes and the encoding from \( \Z_q \) to G."

## Source Map
- [CryptographyV6.pdf](../../subjects/Cryptology/sources/CryptographyV6.pdf) | Page 115-117 | Covers: DL, DH, DDH problems and definitions
- [CryptographyV6.pdf](../../subjects/Cryptology/sources/CryptographyV6.pdf) | Page 117 | Covers: El Gamal cryptosystem (general version), decryption verification (Lemma 9.6)
- [CryptographyV6.pdf](../../subjects/Cryptology/sources/CryptographyV6.pdf) | Page 116 | Covers: Theorem 9.7 (CPA security if DDH hard), Exercise 9.1 (proof sketch)
- [CryptographyV6.pdf](../../subjects/Cryptology/sources/CryptographyV6.pdf) | Page 120 | Covers: Why DDH not hard in \( \Z_p^* \) (Lemma 9.10), safe primes, prime order subgroups
- **Source data missing for LWE problem and cryptosystem** (no details in provided excerpts)