# Interaction design and multimodal interaction

Norman’s Design Principles, affordances, input device properties, transfer/acceleration functions, feedback mechanisms, and multimodal definitions, applications and examples

## The "Elevator Pitch" (Synthesis)

**Explain Interaction design and multimodal interaction to a peer in 3 sentences. Focus on WHY we use it, not just how.**  
> When designing physical devices, it is crucial to consider how users will interact with them. The user's interaction should be analized through the lens of Norman's design principles: visibility, feedback, constraints, mapping, consistency, affordance.
> When designing an input device, desinging the transfer function in a way that feels 'right' is a great task. You want something the user understands intuitively, can control precisely but also fast. For example, when using a joystick it is not obvious how that would controll a motor or an LED.
> In the phisycal world (digital too btw) designing devices that you interact with using multiple modalities can be a great way to have better designs. This enhances users' experience (they are more involved, focus more, get more context etc) and lets you give more detailed and careful feedback.

## Core Vocabulary & Syntax (Total Recall)

| Term                                 | Definition & Context                                                                                                                                                                                                                                                                                                                        |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Norman's Design Principles**       | [Don Norman is one of the funding fathers of cognitive science and HCI. in his 1988 book he described 6 foundational design principles that we still live by: Visibility, Feedback, Constraints, Mapping, Consistency, Affordance.]                                                                                                         |
| **Affordance**                       | [An attribute of an object that allows people to know how to use it; eg. a mouse button invites pushing, a door handle affords pulling - Norman doors. Virtual stuff have ‘perceived’ affordances, PhysComp has both that and 'real'. ]                                                                                                     |
| **Visibility**                       | [Relevant parts of an interaction should be visible (eg. button should clearly be abutton, sensor shouldn't be hidden etc), potentially helped by labels or audio cues if needed.]                                                                                                                                                          |
| **Feedback**                         | [Information sent back to the user after an action has been performet. Audio, visual, haptic...]                                                                                                                                                                                                                                            |
| **Constraints**                      | [Restriction of possible actions of the user to be performed so they don't perform invalid options, eg. key cannot be inserted the wrong way round.]                                                                                                                                                                                        |
| **Mapping**                          | [Relationship between controllers and controllees - which button does what, what the knob turns etc. Effective mapping design ensures the user's mental model aligns closely with the system's conceptual model.]                                                                                                                           |
| **Transfer function**                | ["A transfer function is a mathematical transformation that scales the data from an input device. Usually the goal is to provide more stable and more intuitive control, but a poor transfer function hinders performance. Eg. a force-to-velocity function: the force one exerts on an FSR is mapped to the speed of a motor's rotation."] |
| **Indirect vs Direct Input Devices** | [A direct input device is one that also shows the action of the input eg. a touchscreen]                                                                                                                                                                                                                                                    |
| **Multimodal interaction**           | [Interaction with the virtual and physical environment through multiple natural modes of communication (more than one of: sight, hearing, taste, taste, smell)]                                                                                                                                                                             |

```
Vikings Forget Clothes Making Civilians Anxious
i       e      o       a      o         f
s       e      n       p      n         f
i       d      s       p      s         o
b       b      t       i      i         r
i       a      r       n      s         d
l       c      a       g      t         a
i       k      i              e         n
t              n              n         c
y              t              c         e
               s              y
```

## The "Exam Trap" (Distinctions)

**Distinguish between real affordances and perceived affordances based on GUI vs. Physical Computing contexts.**

| Criterion                             | Real Affordances | Perceived Affordances |
| ------------------------------------- | ---------------- | --------------------- |
| **Definition**                        | [Fill in]        | [Fill in]             |
| **Examples**                          | [Fill in]        | [Fill in]             |
| **Application in Physical Computing** | [Fill in]        | [Fill in]             |
| **Norman’s View**                     | [Fill in]        | [Fill in]             |

## Exam Simulation

**Oral Presentation 1 (2-3 mins):** How would you walk me through **Norman’s Design Principles** (visibility, feedback, constraints, mapping, consistency, affordance) and justify their application to a physical computing prototype? Support with HCI/Psychology references from sources.

**Oral Presentation 2 (2-3 mins):** Present the **definition, advantages, and examples** of multimodal interaction (input/output). Explain why it improves reliability and naturalness in interactive artifacts.

**Follow-up Question:** In your group project prototype, evaluate input device properties (e.g., direct vs. indirect, device acquisition time, occlusion) and transfer/acceleration functions. How do they align with feedback mechanisms (haptic, non-speech audio) for user experience?

- Since input is just button press, transfer functions are not really a thing (although we did have to pay attention to only regard rising edges of button presses).
- multimodality for the 2 modules: visual and haptic.
- feedback for each button press as LED flash added pretty late at the project - came as an idea from the HCI course, realised proper feedback is crucial.
- we realised at IT PaRaDe that it is great to have a feedback when the sequence is over
- audio feedback could be great, but out of scope currently

## Source Map

- [PhysicalComputing_2_IntDesignAndMultimodal](../../subjects/PhysicalComputing/sources/PhysicalComputing_2_IntDesignAndMultimodal.pdf) | Page 3 | Covers: **Norman’s Design Principles**  
- `../../subjects/PhysicalComputing/sources/PhysicalComputing_2_IntDesignAndMultimodal.pdf` | Page 10-11 | Covers: **Affordances** (real vs. perceived)  
- `../../subjects/PhysicalComputing/sources/PhysicalComputing_2_IntDesignAndMultimodal.pdf` | Pages 17-20,22-23 | Covers: **Input device properties**, **transfer functions**  
- `../../subjects/PhysicalComputing/sources/PhysicalComputing_2_IntDesignAndMultimodal.pdf` | Pages 27-31,62 | Covers: **Multimodal interaction** definitions, advantages, feedback  
- **Source data missing for specific group project examples** (use curriculum reflection).