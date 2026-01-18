# Revision Notes: Fitts' Law & Hick-Hyman Law

## Essence of the Topic (The "Why")

**Fitts' Law** and the **Hick-Hyman Law** are foundational models in HCI that predict human performance during interaction tasks. Both laws are grounded in **Information Theory** (Shannon & Weaver, 1949) and quantify how users process information—one for *decision-making* (Hick-Hyman) and one for *motor control* (Fitts')[1][2]. Understanding these laws enables designers to optimize interface layouts, button sizes, and menu structures to minimize user effort and task completion time[2][4].

---

## Key Concepts & Critical Vocabulary

- **Hick-Hyman Law**: Predicts that **reaction time increases logarithmically with the number of choices** available to a user. Formally: \(RT = a + b \cdot H_T\), where \(H_T\) is transmitted information (in bits) and \(a, b\) are empirically determined constants[1][2].

- **Fitts' Law**: Predicts that **movement time is a linear function of task difficulty**, determined by target distance (amplitude, \(A\)) and target width (\(W\)). Formally: \(MT = a + b \log_2(1 + \frac{2A}{W})\)[1][3][4].

- **Index of Difficulty (ID)**: A quantitative measure of task difficulty in Fitts' Law, calculated as \(\log_2(1 + \frac{2A}{W})\), expressed in bits[1][3].

- **Information Capacity**: The maximum amount of information (measured in bits per second) that a human system can process. Fitts reported information processing rates of 7.5–11.5 bits/sec for motor tasks[1].

- **Transmitted Information (\(H_T\))**: In Hick-Hyman Law, the actual information conveyed by a stimulus set, accounting for error rates and conditional probabilities. When error rates are high, \(H_T\) is reduced[1].

---

## Core Mechanism / Logical Flow

### Hick-Hyman Law (Decision-Making Process)

1. User is presented with \(n\) stimulus alternatives, each with probability \(p_i\).
2. **Entropy** of the stimulus set is calculated: \(H = -\sum p_i \log_2(p_i)\) (maximum when alternatives are equiprobable).
3. Reaction time increases **linearly** with transmitted information: \(RT = a + b \cdot H_T\)[1][2].
4. **Key finding**: Even when instructed to work quickly and accept errors, RT remains a logarithmic function of information—error rates do not eliminate the law[1].

### Fitts' Law (Motor Control Process)

1. User must move from a starting position to acquire a target.
2. Task difficulty is quantified by the **Index of Difficulty**: \(ID = \log_2(1 + \frac{2A}{W})\).
3. Movement time increases **linearly** with ID: \(MT = a + b \cdot ID\)[1][3].
4. The mechanism involves **iterative corrections**: the movement is not a single action but a series of corrective sub-movements to achieve accuracy[3].

---

## Critical Distinctions

| Aspect | Hick-Hyman Law | Fitts' Law |
|--------|---|---|
| **Process** | Cognitive (decision-making) | Motor (target acquisition) |
| **Relationship** | \(RT = a + b \cdot H_T\) (linear) | \(MT = a + b \cdot ID\) (linear) |
| **Information Metric** | Bits of stimulus alternatives | Bits of movement difficulty |
| **Design Application** | Menu structure, number of choices | Button/icon size, target placement |
| **Empirical Finding** | RT holds even with high error rates | Information processing rate is constant (~7.5–11.5 bits/sec) |

**Common Confusion**: Both laws predict *linear* relationships with information, but Hick-Hyman applies to *decision time* (how long to choose), while Fitts' applies to *movement time* (how long to reach)[1][2][4].

---

## Exam Focus

**Probable Question Types:**

1. **Multiple-Choice (1 pt each)**: Identify which law applies to a scenario (e.g., "A user must select from 8 menu options" → Hick-Hyman; "A user must click a small button far from cursor" → Fitts').

2. **Essay (up to 6 pts)**: 
   - *Example Question*: "Explain how Fitts' Law can be applied to optimize a mobile interface. What design parameters should you adjust, and why?"
   - *Brief Answer Summary*: Increase target width (\(W\)) and reduce distance (\(A\)) to lower ID and thus movement time. Larger buttons and proximity to common starting positions minimize user effort.

3. **Application/Analysis**: Given interface metrics (e.g., button size, menu depth), predict or compare task completion times using the formulas.

4. **Conceptual Understanding**: Distinguish between the two laws and explain why both are necessary for HCI design (one addresses cognition, the other motor control).

---

## Source Map

- [IntroductionToHCI-3.pdf](../../subjects/Human-Computer%20Interaction/sources/IntroductionToHCI-3.pdf) | Pages 46–50 | Covers: Perception, sensory modalities, and foundational HCI concepts (context for understanding why Fitts' and Hick-Hyman matter).

- [A Comparison of the Hick-Hyman Law and Fitts' Law (Seow, 2005)](http://www2.psychology.uiowa.edu/faculty/mordkoff/infoproc/pdfs/seow%202005.pdf) | Full document | Covers: Detailed mathematical formulations, empirical validation, information theory foundations, and direct comparison of both laws[1].

- [Information Theory - Walker Harden](http://www.walkerharden.com/information-theory) | Full document | Covers: Information Theory context, practical applications to interface design, and empirical study results[2].

- [Lecture 9: Hick's and Fitts' Laws (University of Auckland)](https://www.cs.auckland.ac.nz/courses/compsci345s1c/lectures/2010/Lecture_9_HicksFittsLaw.pdf) | Full document | Covers: Practical design implications, menu optimization, and movement correction mechanisms[3].

- [Five HCI Laws for User Experience Design (MeasuringU)](https://measuringu.com/hci-laws/) | Full document | Covers: Practical UX design applications and real-world implications[4].