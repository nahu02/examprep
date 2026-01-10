## The "Elevator Pitch" (Synthesis)

**Explain Sensors to a peer in 3 sentences. Focus on WHY we use them, not just how.**  
> [Sensors give some input to circuits, like the push of a button or the level of light. They are used so computers can "understand" and react to changes in their environment.]

## Core Vocabulary & Syntax (Total Recall)

| Term                               | Definition & Context                                                                                                                                                                                                                 |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Sensor**                         | [Electrical components that convert physical signals into electrical ones.]                                                                                                                                                          |
| **Potentiometer**                  | [Devices that report linear/logarithmic output. 3 terminals: ground, live and out that is somewhere in-between depending on the input; really an adjustable voltage divider. Mainly rotary or slide pots, but can be soft and bendy] |
| **LDR (Light-Dependent Resistor)** | [A variable resistor, where the resistance level decreases when more light hits the sensor. Can be wired up in a voltage divider for analogue input to MCU. The exact values can be meaningless ]                                    |
| **Accelerometer**                  | [Measures proper or g-force acceleration (static: gravity, dynamic: movement). Contains capacitive plates that move in relation to each other changing their capacitance.]                                                           |
| **Gyroscope**                      | [Measures orientation, using angular momentum.Unit: degrees/s or RPS. Lack of fixed reference (only change). Often combined with acc.meters for accurate motion sensing. ]                                                           |
| **Filter**                         | [A digital filter performs mathematical operations on a sampled, discrete-time signal to reduce or enhance certain aspects of that signal]                                                                                           |
| **Median Filter**                  | [Filter to get rid of outlier values. Uses a window of last N measurements, returns the most common element from the samples. Latency depending on the window size can be quite significant.]                                        |
| **Moving Average**                 | [Filter to smooth out signal. Uses window of last N measurements, returns their average. Latency can again be ann issue; choose window size carefully.]                                                                              |


## Exam Simulation

**Follow-up Q&A:** "For your group project, justify sensors chosen vs. alternatives considered (e.g., potentiometer vs. rotary encoder). Ground in HCI/UX rationale."

> Our project used only buttons as sensors (Simon says with lights and buzzers). We have considered using piezzo components as both buzzer motors and button press sensing (all in one), but after testing we concluded that they neither buzzed strong enough, nor did they have the satisfying tactile feel of pressing a button. 

**Follow-up Q&A:** "Explain why you'd select median vs. moving average filter for project sensor noise. Calculate sample output for noisy accelerometer data."

> Median filtering is best for disregarding outlier values, while MA smooths the signal. If I had to choose I'd consider the nature of the sensor, and what I want to use it for. If the sensor may sometimes reports outlier samples, like an ambient light sensor, median sampling works better (you wouldn't want to lighten the backlight of a phone screen just because there was  flash of light in the dark). (However, if I were using the light sensor to measure the small differences in the light given by the sun a MA may be better, as we don't want to completely disregard outliers.) The movement sensing done by an IMU lends itself better for averaging - you usually want to see how the movement changes dynamically if smoothed out. (Like in the bike lamp assignment.)

**Project/Curriculum Q:** "Reflect on your prototype: Evaluate one sensor's integration with 3D print (ergonomics/feedback). Support with scientifically grounded argument from psychology/multimodal interaction."

## Source Map

- [PhysicalComputing_5_Sensors.pdf](../../subjects/PhysicalComputing/sources/PhysicalComputing_5_Sensors.pdf) | Pages 3,5-39,41,43,45-46,48-51,54 | Covers: Sensor definition, types (occupancy/motion/position/movement/touch/force/etc.), examples (potentiometers/FSRs/capacitive/piezo/IMU/LDR/etc.), data conversion, filters.
- [PhysicalComputing_2_IntDesignAndMultimodal.pdf](../../subjects/PhysicalComputing/sources/PhysicalComputing_2_IntDesignAndMultimodal.pdf) | Pages 14-16 | Covers: Input devices, linear/rotary properties, dimensions.