## Overview
This subtopic covers **fundamental electronic components** (resistors, diodes, capacitors, crystals, transistors) and core principles like **Ohm's Law** and **circuit configurations** (series vs. parallel), essential for building and debugging breadboard prototypes with ATmega microcontrollers.

## Key Concepts to Master
- **Ohm's Law** relates _voltage_, _current_, and _resistance_ in a circuit: $V = I \times R$.
- **Resistors** limit current flow and are used in _series to make voltage_ dividers to _scale down voltages_ or create variable voltages from resistance-variable sensors (e.g. _photoresistors_).
- In **series circuits**, total resistance is the _sum_ of individual resistances; current is the _same_ through all components.
- In **parallel circuits**, total resistance is calculated using _the replus_ formula: _ $\frac{1}{R_{total}} = \frac{1}{R_1} + \frac{1}{R_2} + \dots$ _; voltage is the _same_ across all branches.
- **Diodes** allow current to flow in one _way_ only and protect against _reverse voltage and voltage spikes_ in inductive loads like motors.
- **Capacitors** store and release _energy as needed_. Used with crystals for _accurate_ timing in microcontrollers.
- **Crystals** (e.g., 16 MHz) provide _more stable_ clock signal; pair with _capacitors when wiring it to the microcontrollers `OSC1` and `OSC2` pins_ (18-22 pF).
- **BJTs** are controlled by _a small current_ at the base; **MOSFETs** by _some voltage_ at the gate.
- **Circuit Diagrams** must follow layout guidelines: _lower/higher voltages_ at bottom/top, flow from _left_ (inputs) to _right_ (outputs).
- Use **multimeter** to measure _voltage_ (parallel), _current_ (series), _resistance_ (probes on legs).

## Definitions (Fill These In)
- **Voltage**: _Difference in levels of energy between 2 points of a circuit. Compared to **water pressure** when using the water-in-tubes analogue for circuits. Measured in Volts_
- **Current**: _The ammount of energy passing through a point in a circuit. Compared to the **flow of water** when using the water-in-tubes analogue for circuits. Measured in Amps_
- **Resistance**: _The measure of how much a component blocks current flowing through itself. Compared to **pipe width** when using the water-in-tubes analogue for circuits. Measured in Ohms_
- **Ground (GND)**: _The relative null energy level in a circuit (0V)._
- **Flyback Diode**: _A specific use of a diode in a circuit, when it protects a component (e.g. microcontroller) from a voltage spike from an inductive component (e.g. motor or relay)_
- **Voltage Divider**: _The use of 2 resistors to scale down some voltage. Depending on the resistors, any live voltage can be scaled down to any desireable level._ $V_{out} = V_{in} \frac{R_2}{R_1+R_2}$

## Important Distinctions

| Concept              | Series                                     | Parallel                                                      |
| -------------------- | ------------------------------------------ | ------------------------------------------------------------- |
| **Current**          | Same through all components                | Splits between branches                                       |
| **Voltage**          | Drops across each component                | Same across all branches                                      |
| **Total Resistance** | $R_{total} = R_1 + R_2 + \dots$            | $\frac{1}{R_{total}} = \frac{1}{R_1} + \frac{1}{R_2} + \dots$ |
| **Common Use**       | _Voltage dividers, current limiting, etc._ | Multiple loads from one source                                |

- **BJT vs MOSFET**: BJT needs _base_ current to switch; MOSFET needs _gate_ voltage (lower power).
- **Measure Voltage vs Current**: Voltage in _parallel_; current in _series_ with load.

## Example to Reproduce
Draw a schematic for a simple LED blink circuit with ATmega.

## Likely Exam Questions
1. Explain **Ohm's Law** and calculate resistance for a 5V circuit with 20mA current. Draw symbol for series resistors.
2. Present (2-3 min): Difference between series/parallel for sensors/actuators; justify with breadboard example from project.
3. How do you use a multimeter to debug a non-working crystal + capacitors on ATmega? Cite datasheet checks.
4. Describe flyback diode in motor circuit; why shared GND? Sketch schematic.
5. For prototype: Choose BJT or MOSFET for actuator; support with HCI/psychology (e.g., response time).

## Sources to Read

| PDF                                                                                                                                                                                                  | Pages             | Why Read                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| [1_Basic Electronic Components - Physical Computing 2025 - Copy.pdf](../../subjects/Physical%20Computing/sources/1_Basic%20Electronic%20Components%20-%20Physical%20Computing%202025%20-%20Copy.pdf) | 6, 14-15          | Core components overview, circuits, series/parallel, Ohm's Law                                                                |
| [5_Debugging Prototypes - Physical Computing 2025.pptx.pdf](../../subjects/Physical%20Computing/sources/5_Debugging%20Prototypes%20-%20Physical%20Computing%202025.pptx.pdf)                         | 3,5,8,10-21,23    | Multimeter use, datasheets (voltage/current/resolution/pin configs), debugging components like resistors/caps/diodes/crystals |
| [PhysicalComputing_1_Intro.pdf](../../subjects/Physical%20Computing/sources/PhysicalComputing_1_Intro.pdf)                                                                                           | 22-23,27-28       | Assignment 1 schematics/breadboards: symbols, layout, component descriptions                                                  |
| [3_Powering Prototypes - Physical Computing 2025.pdf](../../subjects/Physical%20Computing/sources/3_Powering%20Prototypes%20-%20Physical%20Computing%202025.pdf)                                     | 10,27,30,32,42-43 | GND, current loops, flyback diodes, voltage dividers for sensors/motors                                                       |
| [2_Microcontrollers - Physical Computing 2025.pdf](../../subjects/Physical%20Computing/sources/2_Microcontrollers%20-%20Physical%20Computing%202025.pdf)                                             | 13,44-47          | Schematics, crystal/caps debugging, multimeter, blink LED example                                                             |
| [PhysicalComputing_12_PCBs.pdf](../../subjects/Physical%20Computing/sources/PhysicalComputing_12_PCBs.pdf)                                                                                           | 16,24             | Schematic layout tips (flow, voltages)                                                                                        |