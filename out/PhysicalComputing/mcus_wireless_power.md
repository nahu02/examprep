# Microcontrollers, communication protocolls, PCB design, power management

"What are microcontrollers, advantages/ disadvantages, microcontroller architecture (pins, ADC, memory), protocols (I2C, SPI, UART), ADC, PCB design (materials, board layout, SMT, through-hole, Fusion360 Eagle and DRC), wireless (Bluetooth, RFID, NFC), and power management (batteries [battery power, series vs parallel], DC-DC converters, using multiple power sources), calculating voltage/current/power requirements"


## The "Elevator Pitch" (Synthesis)

**Explain MCUs, wireless comms, and power to a peer in 3 sentences. Focus on WHY we use it, not just how.**  
> MCUs are very powerful - basically cheap tiny computers we can program however we want. They're in everything from washing machines to cars because they are extremely practical and make it easy to describe behavioural logic with code.
> There are many wired (I2C, SPI, UART) and wireless (RF, RFID & NFC, WiFi, Bluetooth, Zigbee...) standards that each suit a different specific need. Some are useful for fast point-to-point (P2P) comm, some are usable in a mesh, some are cheap etc.
> To power your circuit you need to pay attention to supplying both the right voltage and the right current. You can (with some loss) convert voltage up/down with DCDC converters (buck/boost). If you use multiple power sources (eg. 2 batteries) you want to share the ground (so all components have the same relative 0V), and you can decide whether you want to increase the capacity (connect batteries in parallel) or increase the voltage (connect them in series). 

## Core Vocabulary & Syntax (Total Recall)

| Term                                    | Definition & Context                                                                                                                                                                                                                                 |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Microcontroller (MCU)**               | [Microcontrollers are small computers in an SoC format - they include a CPU, memory, I/O pins, optionally a few kB flash storage]                                                                                                                    |
| **ATmega328**                           | [An 8MHz AVR MCU (can use up to 16MHz with external crystal). Has >=20 I/O pins, hardware UART, 32 kB of program memory ]                                                                                                                            |
| **ADC (Analog-to-Digital Converter)**   | [The ADC used in most microcontrollers uses a DAC (digital-to-analog) and a comperator, and esentially runs binary search on the DAC results]                                                                                                        |
| **I2C (Inter-Integrated Circuit)**      | [Wired com protocol that uses a single bus, a built in clock and only 2 wires. It uses 1 controller and multiple agents where agents are directly adressable via their address. Very easy to scale.]                                                 |
| **SPI (Serial Peripheral Interface)**   | [Wired com protocol with pins MISO, MOSI, SPC, and one SS pin for each agent. Great for fast/complex communication; used for flashing atmega chips and connecting flash/EEPROM storage. ]                                                            |
| **UART/USART (Univ Async Rec-Trans)**   | [Wired com protocol usually bw 2 devices. RX/TX pins used for serial communication, for USART there's a clock wire too. Best for long distance P2P communication (eg. Serial Monitor)]                                                               |
| **AVCC**                                | [Alternate VCC. A pin on Atmega chips used in the ADC. Should always be connected externally to the VCC pin, as per the manufacturer's instructions.]                                                                                                |
| **SMT (Surf Mnt Tech) vs Through-hole** | [Different techniques of soldering components to a PCB. SMT is cheaper, provides better connections, allows for higher density; but Through-hole is easier to work with manually and easier to debug.]                                               |
| **DRC (Design Rule Check)**             | [A Design Rule Check is a function in PCB software (Eagle/Fusion360) used to prevent manufacturing errors. LabTools provides a ruless file that ensures the design will work on the lab's PCBs.]                                                     |
| **Bluetooth (BLE vs Classic)**          | [Wireless com protocol design for P2P communication in 2.4GHz spectrum. Classic has faster speeds (50Mbps vs 2Mbps) and longer range (100m vs 30m) but it consumes more energy and supports fewer simultaneous connections (7 vs 128)]               |
| **RFID / NFC**                          | [RFID uses active/passive (self-powered) tags that store mainly identity info. NFC is a subset of the protocol for small distances where a device can be (but not always, and not at the same time) both an initiator and a target.]                 |
| **Series vs Parallel (Battery)**        | [When connecting multiple batteries, one can choose to increase the Voltage (connect in series) vs Capacity (connect in parallel)]                                                                                                                   |
| **DC-DC Converter (Buck/Boost)**        | [Used to step down(buck) / up(boost) voltage. Stepping down is generally more efficient, but depends on how much. We used a Low Dropout Regulator in our project to step down 3.7-4.2V to a constant 3.3V. $P_{total}=\frac{efficiency}{P_{load}}$ ] |
| **Shared ground**                       | [When using multiple power rails, you want to still connect the grounds in series. This is because when components on different rails communicate, they should have a shared concept of 0V. It's also important for the current flow.]               |
| **Flyback Diodes**                      | [A diode connected across an inductor (the motor) used to stop the voltage spike seen across an inductive load when its supply current is suddenly reduced or interrupted.]                                                                          |
| **Power**                               | [Power consumption is the rate at which a device or circuit uses electrical energy per unit of time: a high-wattage device pulls energy from the source quickly. It is calculated as $P = I \times V$  ]                                             |

## Logic Flow / Mechanism (Process)

### PCB Design Workflow (Eagle/Fusion360)
1. **Schematic Design:** [Describe process: nets, values, symbols]
2. **Board Layout:** [Describe process: placement, routing, board shape]
3. **DRC (Design Rule Check):** [Explain what this checks and why it is crucial]
4. **Manufacturing Export:** [List file types generated for production]
5. !!

### Power Management Calculation
1. **Calculate Total Current:** [Sum component requirements based on datasheets or measurements (using Ampmeter in series). It's best to round up. If some components require a lot of current (eg. motors) it is best to give them their own power source.]
2. **Determine Voltage Req:** [Examine the datasheets of all components and identify the voltage range suitable for all components. If no value can be found, split power into multiple rails and use a DCDC converter to step up/down.]
3. **Select Battery:** [You want a battery of the right nominal voltage, rechargeability, capacity and potentially chemistry. Multiple batteries may be connected together to increase voltage or capacity, but many chargers will not work for multi-cell batteries.]

## The "Exam Trap" (Distinctions)

**Contrast I2C, SPI, U(S)ART:**

| Feature       | I2C (Inter-Integrated Circuit)              | SPI (Serial Peripheral Interface)                    | UART (Universal Asynchronous Receiver-Transmitter) |
| :------------ | :------------------------------------------ | :--------------------------------------------------- | :------------------------------------------------- |
| **Pins**      | [Just 2: SDA, SCL]                          | [MISO, MOSI, SCL; SS for each agent ]                | [RX, TX, clock for USART]                          |
| **Type**      | Sync, Multi-controller, Bus                 | Sync, Single-controller, Bus                         | Async, P2P (Point-to-Point)                        |
| **Best for**  | [Controlling many agnets, simple, scalable] | [Fast/complex architecture, connecting flash/EEPROM] | [Long distance P2P]                                |
| **Used when** | [Our project!]                              | [Flashing atmega chips]                              | [Serial Monitor in Arduino IDE]                    |


**Distinguish Power Configurations:**
| Configuration | Effect on Voltage $V_{total}$ | Effect on Capacity $Ah_{total}$ |
| :------------ | :---------------------------- | :------------------------------ |
| **Series**    | [ $V_1 + V_2 + \dots$ ]       | [ unchanged ]                   |
| **Parallel**  | [ unchanged ]                 | [ $Ah_1 + Ah_2 + \dots$ ]       |


**Distinguish Wireless Protocols:**
| Protocol                | Range        | Power        | Typical Use Case |
| :---------------------- | :----------- | :----------- | :--------------- |
| **Bluetooth (Classic)** | [Fill Range] | [Fill Power] | [Fill Use Case]  |
| **BLE (Low Energy)**    | [Fill Range] | [Fill Power] | [Fill Use Case]  |
| **RFID/NFC**            | [Fill Range] | [Fill Power] | [Fill Use Case]  |

## Exam Simulation

**Oral Presentation 1 (2-3 mins):** How would you present **microcontroller advantages/disadvantages** for a battery-powered prototype? Structure as: definition, pros/cons list, link to project rubric (e.g., no Arduino, custom PCB).

**Follow-up Q:** Explain why actuators need secondary power supplies despite MCU pins – reference voltage/current limits and ground rule.

> They may need higher current/voltage than the MCU can provide. In these cases the MCU may just power a trasistor to switch the component on/off - this is what we do in our project for motors.

**Oral Presentation 2 (2-3 mins):** Walk through **communication protocols** for sensors/actuators on ATmega328 – pick 2, detail pins and when to use each vs GPIO.

**Follow-up Q:** Justify AVCC connection in debugging – what fails without it?

> It is needed for ADC conversion, but the manufacturer says always to connect it to voltage, so other internal components may start failing too. I read someone saying the external clock may start drifting too.

**Project-Based Q:** Analyze a specific design challenge your group faced when integrating components onto the custom PCB (e.g., mixing 3.3V and ~3.7V logic). How did you resolve it in the schematic or board layout?

!!

**Calculation Q:** You have a 3.7V 2000mAh LiPo battery and a circuit drawing 500mA at 5V (via a Boost converter).
1. Calculate the power consumption of the circuit. [ $P' = V_{out} \times I_{out} = 5V \times 0.5A = 2.5W$ after DCDC, but assuming some efficiency $\eta = 80%$ (pretty low estimate) the power consumption of the circuit is $P = \frac{P}{\eta} = \frac{2.5W}{0.8} = 3.125W$]
2. Calculate the effective current draw from the battery. [ $I_{batt} = \frac{P_{load}}{V_{batt}} = \frac{3.125W}{3.7V} = 845mA$ ]
3. Estimate battery life. [ $T = \frac{Cap}{I} = \frac{2000mAh}{845mA} = 2.37h$ ]

**Efficiency Calculation Q:** A linear regulator (LDO) drops 9V to 5V for a circuit drawing 100mA.
1. Calculate Power In and Power Out. [$P_{in} = 9V \times 0.1A = 0.9W$ and $P_{out} = 0.5W$]
2. Calculate the efficiency. [$\eta = \frac{P_{out}}{P_{in}} \times 100\% = 55.56\%$]
3. Calculate the power dissipated as heat. [ $P_{waste} = P_{in} - P_{out} = 0.4W$ ]

**Wireless Q:** Compare Bluetooth vs RFID for an interactive museum exhibit where users "collect" items. Which would you choose and why? (Hint: Range, user action, power).

Bluetooth communication requires pairing - that's not the best for the visitors. It's better to touch readers to NFC tags - that's cheap and easy, and the data can just be stored on the reader (only ID on the tags, logic on what to do on reader).

## Source Map
| Source                                                                                                                                 | Page(s)            | Covered topic(s)                                                                                   |
| -------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | -------------------------------------------------------------------------------------------------- |
| [1_Intro.pdf](../../subjects/PhysicalComputing/sources/PhysicalComputing_1_Intro.pdf)                                                  | 14,27,28           | project reqs (PCB, 3D print, power, polish), rubrics                                               |
| [2_Microcontrollers](../../subjects/PhysicalComputing/sources/2_Microcontrollers%20-%20Physical%20Computing%202025.pdf)                | 3-8,11-14,16-22,46 | MCU def, adv/disadv, types (AVR/ATmega), pins, memory, clocks, protocols (I2C/SPI/UART), ADC, GPIO |
| [6_Actuators](../../subjects/PhysicalComputing/sources/PhysicalComputing_6_Actuators.pdf)                                              | 20                 | power for actuators vs MCU pins                                                                    |
| [5_Debugging Prototypes](../../subjects/PhysicalComputing/sources/5_Debugging%20Prototypes%20-%20Physical%20Computing%202025.pptx.pdf) | 6,9                | ATmega issues, AVCC                                                                                |
| [12_PCBs](../../subjects/PhysicalComputing/sources/PhysicalComputing_12_PCBs.pdf)                                                      | 2                  | PCB basics (incomplete in extract)                                                                 |