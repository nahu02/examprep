# Empirical Evaluation (Experiments) in HCI: Revision Notes

## Essence of the Topic (The "Why")

**Empirical evaluation** is the systematic, scientific approach to assessing whether interactive systems work as intended and deliver value to users. In HCI, experiments represent a specific type of empirical evaluation that uses **controlled conditions and hypothesis testing** to compare the usability of different user interfaces by measuring quantifiable outcomes like task completion time, error rates, and user satisfaction. This rigorous methodology is essential because it moves beyond intuition or theory alone, grounding design decisions in measurable evidence about human performance and user experience.

---

## Key Concepts & Critical Vocabulary

- **Empirical Research**: Collecting data through direct observation or experiments to verify or disprove hypotheses about how people interact with computers.

- **Hypothesis (Testable)**: A clear, measurable prediction about user interface performance that can be quantified and tested—for example, "Interface X is faster to access than Interface Y".

- **Dependent Variables**: The specific measurements you collect during an experiment to test your hypothesis; typical examples include **time to complete task**, **error rate**, **event count**, and **subjective satisfaction ratings**.

- **Independent Variables**: The factors under the researcher's control that are manipulated to test their effect—such as user groups, devices, or interface designs.

- **Usability**: The degree to which an interactive system is practical, learnable, efficient, error-resistant, and satisfying; all dimensions can be quantified for experimental comparison.

---

## Core Mechanism / Logical Flow

**The Controlled Experiment Process:**

1. **Formulate a testable hypothesis** — State a clear, quantifiable prediction about how two or more interface designs will differ in performance.

2. **Define dependent variables** — Identify what you will measure (time, errors, satisfaction) to test the hypothesis.

3. **Design experimental conditions** — Control variables of no interest (user groups, tasks, environment) to isolate the effect of the independent variable (the interface design).

4. **Conduct the study with real users** — Have representative users perform representative tasks with the interfaces being compared.

5. **Analyze results using statistical tests** — Apply statistical methods to determine whether observed differences are significant enough to accept or reject the hypothesis.

---

## Critical Distinctions

### **Experiment vs. User Study**

- **Experiment**: A **controlled comparison** of at least two user interfaces under standardized conditions, designed to measure specific usability dimensions with high precision and clean comparisons. Offers **limited realism** but **high precision**.

- **User Study** (broader term): Any empirical investigation involving users; includes experiments, usability tests, think-aloud tests, and deployment studies. User studies can be formal or ad hoc.

### **Laboratory vs. Field Evaluation**

| Aspect               | Laboratory                           | Field                                |
| -------------------- | ------------------------------------ | ------------------------------------ |
| **Setting**          | Controlled, away from context of use | Real-world, during actual system use |
| **Control**          | High—variables can be isolated       | Low—many uncontrolled factors        |
| **Realism**          | Lower—artificial conditions          | Higher—natural use conditions        |
| **Generalizability** | May be limited to lab context        | Findings reflect real-world use      |

### **Analytical vs. Empirical Evaluation**

- **Analytical**: Evaluator compares interface to guidelines or theories *without involving users*; inexpensive but prone to false positives.

- **Empirical**: Users' actual interactions with the system form the basis for evaluation; direct assessment of usability but may miss broader context.

---

## Research Strategy: McGrath's Three Principles

**Realism, Precision, and Generalizability Trade-offs**:

- **Realism**: How similar the study situation is to real-world use (field studies are high in realism).
- **Precision**: How much accuracy and control over variables (lab experiments are high in precision).
- **Generalizability**: How well findings apply to other people or situations (large surveys are high in generalizability).

**Key insight**: These three criteria conflict with each other. Maximizing realism (field study) reduces precision and generalizability; maximizing precision (controlled lab experiment) reduces realism.

**Triangulation**: Combine multiple research methods with different strengths and weaknesses to compensate for each method's limitations and strengthen overall conclusions.

---

## Methodological Quality: Four Dimensions

**Validity**: Whether conclusions drawn from a study are justified.
- **Internal validity**: Does the researcher's controlled variable (e.g., interface design) actually affect observations?
- **Construct validity**: Does the measurement actually measure what it claims (e.g., does a questionnaire truly measure user satisfaction)?
- **Statistical conclusion validity**: Are conclusions statistically reliable?
- **External validity**: Do conclusions hold for other participants and settings?

**Reliability**: Whether the research produces consistent results if applied again to the same context in the same way.

**Transparency**: Researchers make their design, data, analysis, and conclusions accessible and inspectable to enable replication.

**Ethics**: Careful consideration of what is right and wrong in collecting, analyzing, and reporting data; includes obligations to research participants.

---

## Exam Focus

### **Probable Question Types:**

**Multiple-Choice (1 point each):**
- Identify the dependent variable in a given experiment scenario.
- Distinguish between internal and external validity threats.
- Recognize which research method (experiment, survey, field study) best fits a given research goal.
- Explain the trade-off between realism and precision.

**Essay Questions (up to 6 points each):**
- **Example Essay Question**: "You are designing an experiment to compare two menu bar designs (anchored vs. separated). Describe your testable hypothesis, identify your dependent variables, explain how you would control for confounding variables, and discuss one threat to internal validity and one to external validity."

  **Brief Answer Summary**: State hypothesis (e.g., "Anchored menu bar is faster to access"). Dependent variables: task completion time, error rate, subjective satisfaction. Control: same users, same tasks, same environment. Internal validity threat: user experience level. External validity threat: lab setting may not reflect real-world distractions.

- **Example Essay Question**: "Explain McGrath's three principles of research strategy (realism, precision, generalizability) and why it is impossible to maximize all three simultaneously. Provide a concrete example."

  **Brief Answer Summary**: Define each principle. Explain trade-offs: high realism (field study) introduces uncontrolled variables, reducing precision and generalizability to other contexts. Example: studying real office workers in their natural environment reveals authentic behavior but makes it hard to isolate which interface feature caused the effect or whether findings apply to other offices.

---

## Source Map

| Source                                              | Coverage                                                                                                                                       |
| --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Wikipedia: Human–computer interaction               | Defines HCI and empirical measurement; introduces quantitative usability metrics (time, errors)                                                |
| HCI 101: Summary of Chapter 4                       | Explains empirical research methodology, hypothesis testing, and the scientific approach in HCI                                                |
| MIT Reading 11: Experiment Design                   | Core framework: testable hypotheses, dependent variables, controlled experiments, statistical testing                                          |
| Georgia Tech: Quantitative and Qualitative Modeling | Distinguishes quantitative vs. qualitative evaluation; introduces analytical vs. empirical methods                                             |
| Oxford Academic: Introduction to Evaluation         | Comprehensive coverage of validity types, reliability, transparency, ethics, and McGrath's three principles; laboratory vs. field distinctions |