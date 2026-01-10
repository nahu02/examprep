# Actuators Study Scaffold: Desirable Difficulty Edition

## The "Elevator Pitch" (Synthesis)
**Explain actuators to a peer in 3 sentences. Focus on WHY we use them in Physical Computing projects, not just how.**  
> Actuators are components that move a mechanism. Most trivially, this includes electric motors that are used for rotating, displacing, pushing/pulling (solenoids), tightening/loosening things, or to give haptic feedback via vibrations. actuators can also be non-electrical in nature (pneumatic, hydraulic), or they may be smart materials like Shape-Memory Alloys (SMA), that reversibly change their shape based on the temperature.

## Core Vocabulary & Syntax (Total Recall)
| Term                             | Definition & Context                                                                                                                                                                                                                            |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Actuator**                     | [Components that move mechanisms. Can be electric or otherwise.]                                                                                                                                                                                |
| **DC Brush Motor**               | [Electric motor that creates rotational movement using magnets internally. Brush wears down with time. Only has 2 pins: direction of rotation depends on which one is live and which is ground. Cheap and can provide high torque.]             |
| **Servomotor**                   | [Electric motor that creates rotational movement. Can be told where to turn to precisely, they correct for errors. Wires: power, ground and control. Attachments ("horns") can be attached to the shaft, to fit the device they are operating.] |
| **Stepper Motor**                | [A kind of brushless DC motor that has discrete positions it can assume. This makes it precisely controllable and predictable. Stepper motors are typically controlled using digital pulses instead of constant current. ]                      |
| **Solenoid**                     | [Type of motor that controls a linear push/pull motion. They only have an on/off position.]                                                                                                                                                     |
| **H-Bridge**                     | [Circuit for DC brush motor control, where you may want to reverse the polarity of the different pins to drive a motor clockwise or anticlockwise. Needs 4 switches / transistors.]                                                             |
| **PWM (Pulse-Width Modulation)** | [Way to control speed of a motor by cyclically turning it off and on. By changing or modulating the timing of these pulses the speed of the motor can be controlled ie, the longer the pulse is “ON”, the faster the motor will rotate.]        |

## The "Exam Trap" (Distinctions)
**Distinguish DC Motors, Servos, and Steppers based on motion control, power needs, and project fit. Fill the matrix from sources only.**

| Criterion             | DC Brush Motor                    | Servomotor                       | Stepper Motor                     |
| --------------------- | --------------------------------- | -------------------------------- | --------------------------------- |
| **Motion Type**       | [Continuous]                      | [Instructed position]            | [Incremental steps]               |
| **Direction Control** | [Reverse polarity (use H-bridge)] | [Control wire]                   | [wiring (H-bridge) or via driver] |
| **Speed Control**     | [voltage or PWM]                  | [control wire (built-in driver)] | []                                |

## Exam Simulation
**Oral Exam Prep: 2-3 min Presentation + Q&A**  
1. **Presentation Topic 1:** "Walk me through controlling motors in your group project. Why H-Bridge + PWM over direct voltage? Reference powering risks." *How would you answer in 2-3 mins? Practice aloud.*  

> We used 4 linear resonant actuators (vibration motors) in the project. They only ever need to be on/off, so we only wired it to ground and 3.4V. (The 3.4V was converted down form the 3.7-4.2V of the battery, to stay in the safe operation range of the LillyPad vibration motors.) Since motors are quite delicate, we were careful to have a separate power rail just for motors, to regulate the voltage carefully, and to protect other components against voltage spikes.

2. **Follow-up Q&A:** "Your project used [your actuators]. Explain trade-offs in powering (voltage, flyback diode) and control." *Simulate response under 1 min.*

> The motors were wired with a flyback diode and in parallel with them (from ground to live) to catch any inductive loads, and a resistor limiting the current flowing to them (with $3.4V$ using Ohm's law and their rated max current of $75mA$, this worked out to $\frac{3.4V}{75mA} = 45.3\Omega$).

## Source Map
- [PhysicalComputing_6_Actuators.pdf](../../subjects/PhysicalComputing/sources/PhysicalComputing_6_Actuators.pdf) | Page 3 | Covers: Actuator definition, energy sources  
- [PhysicalComputing_6_Actuators.pdf](../../subjects/PhysicalComputing/sources/PhysicalComputing_6_Actuators.pdf) | Pages 6-18,23,26 | Covers: Motor types (DC, Servo, Stepper, Solenoid), H-Bridge, PWM, other actuation  
- [3_Powering Prototypes - Physical Computing 2025.pdf](../../subjects/PhysicalComputing/sources/3_Powering%20Prototypes%20-%20Physical%20Computing%202025.pdf)| Pages 35-44 | Covers: Powering actuators, PWM mapping, circuit protections, exercises