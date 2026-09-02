"""Embedded System Design (AEZG512 / AELZC512) Comprehensive Topic Dataset.
Covers Embedded Systems, ARM Cortex-M4 Core Architecture, Memory Map, Boot Sequence, Thumb-2 Assembly,
NVIC Exceptions, NXP S32K144 MCU, Embedded C, GPIO, Timers, PWM, ADC, UART, SPI, I2C, FlexCAN, and Remote Labs.
"""

SUBJECT_METADATA = {
    "title": "Embedded System Design",
    "code": "AEZG512 / AELZC512",
    "credits": "1-1-2 (4 Units)",
    "description": "Hardware and software design of modern automotive embedded systems: ARM Cortex-M4 processor architecture, Thumb-2 assembly programming, NVIC exception handling, NXP S32K144 automotive MCU peripheral drivers (GPIO, LPIT, FTM PWM, ADC, LPUART, FlexCAN), and remote lab workflows.",
    "lead_instructor": "Prof. S. S. Kendre & Prof. Shree Prasad M., BITS Pilani"
}

TOPICS = [
    {
        "slug": "embedded-systems-overview-and-classification",
        "title": "Embedded Systems Foundations & Real-Time Constraints",
        "module": "Embedded Fundamentals",
        "level": "Beginner",
        "importance": 5,
        "overview": "An embedded system is an application-specific, purpose-built computing system that integrates processing cores, memory, and specialized hardware peripherals into a larger mechanical or electrical product. In automotive engineering, embedded systems operate under stringent real-time deterministic constraints, strict safety standards (ISO 26262 ASIL), low power consumption limits, and harsh environmental conditions.",
        "learning_objectives": [
            "Define an embedded system and distinguish it from general-purpose computing systems.",
            "Analyze the fundamental characteristics: Purpose-built, Reactive/Real-time, Resource-constrained, and High Reliability.",
            "Differentiate between Hard Real-Time, Soft Real-Time, and Firm Real-Time systems.",
            "Classify embedded systems based on generation, complexity, and deterministic performance requirements."
        ],
        "prerequisites": "Basic computer science fundamentals, binary/hexadecimal numbering, digital logic.",
        "core_concept": "A laptop is a general-purpose computer: you can play games, edit spreadsheets, or browse the web; if it freezes for 200 ms, you are annoyed but nobody gets hurt. An Anti-Lock Braking System (ABS) ECU is a hard real-time embedded system: it runs only one dedicated control program, and if it fails to calculate wheel slip or misses a braking deadline by 5 milliseconds, the vehicle skids out of control, causing a fatal accident.",
        "lecture_notes": "Lecture 1 of Embedded System Design delivered by Prof. S. S. Kendre introduced the foundational definitions of embedded computing. The professor stressed: 'An embedded system is not a standalone desktop PC. It is embedded inside a host machine to perform one dedicated control function with hard deterministic timing.' The lecturer traced the historical evolution from 1st generation 4-bit/8-bit microcontrollers (Intel 8051) to 4th generation System-on-Chips (SoCs) and multicore 32-bit ARM Cortex-M4 processors powering modern automotive ECUs.",
        "extra_explanation": "Let's analyze the core classification criteria:\n\n1. **Real-Time Determinism Categories:**\n   - **Hard Real-Time System:** A deadline missed is a catastrophic system failure (e.g., Airbag deployment squib ignition $< 10\\text{ ms}$, Engine Spark Timing $< 100\\ \\mu\\text{s}$, Anti-Lock Braking modulation).\n   - **Firm Real-Time System:** Infrequent deadline misses do not cause catastrophe, but the delayed result is completely useless and discarded (e.g., V2X cooperative awareness collision warnings).\n   - **Soft Real-Time System:** Deadlines are desirable, but occasional latency degradation merely reduces quality of service (QoS) without system failure (e.g., Infotainment touch screen response, cabin ambient lighting transitions).\n\n2. **Classification by Complexity & Generation:**\n   - **Small-Scale Embedded Systems:** 8-bit / 16-bit microcontrollers (e.g., Microchip PIC, 8051), battery-powered, written in assembly/C, simple door switches.\n   - **Medium-Scale Embedded Systems:** 16-bit / 32-bit microcontrollers (e.g., ARM Cortex-M0/M3/M4, NXP S32K144), hardware timers, ADC, CAN buses, RTOS (FreeRTOS, OSEK/AUTOSAR).\n   - **Sophisticated / Large-Scale Systems:** 32-bit / 64-bit multi-core processors (e.g., ARM Cortex-A53/A72, NVIDIA Orin), running embedded Linux/QNX for ADAS camera perception and autonomous navigation.",
        "workflow_steps": [
            ("Sensory Signal Event", "Physical sensor converts real-world stimulus to voltage"),
            ("Hardware Interface / ADC", "Peripherals capture and condition the digital signal"),
            ("Deterministic Processing", "Cortex-M4 core executes control algorithm within strict deadline"),
            ("Actuator Driver Output", "GPIO / PWM outputs command to physical actuator"),
            ("Continuous Reactive Loop", "System returns to wait-for-interrupt (WFI) low power mode")
        ],
        "diagram_ascii": """
+-----------------------------------------------------------------------------------+
|               GENERIC AUTOMOTIVE EMBEDDED SYSTEM ARCHITECTURE                      |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|           PHYSICAL ENVIRONMENT                     EMBEDDED MICROCONTROLLER       |
|                                                  +-----------------------------+  |
|      +---------------------+                     | +---------+     +---------+ |  |
|      | Analog Sensors      |                     | | ARM     |     | FLASH   | |  |
|      | (Wheel Speed / Temp)|-----[ ADC Module ]->| | Cortex  |<===>| Memory  | |  |
|      +---------------------+                     | | M4 Core |     | (Code)  | |  |
|                                                  | +----+----+     +---------+ |  |
|      +---------------------+                     |      |          +---------+ |  |
|      | Digital Switches    |-----[ GPIO Ports ]->|      +=========>| SRAM    | |  |
|      | (Brake / Ignition)  |                     |      | (Bus)    | (Data)  | |  |
|      +---------------------+                     |      v          +---------+ |  |
|                                                  | +----+----+     +---------+ |  |
|      +---------------------+                     | | Timers  |     | CAN /   | |  |
|      | Actuators / Motors  |<----[ FTM / PWM ]---| | (LPIT)  |     | LPUART  | |  |
|      | (Throttle / Brakes) |                     | +---------+     +----+----+ |  |
|      +---------------------+                     +----------------------|------+  |
|                                                                         |         |
|                                                 ========================+=====    |
|                                                 Vehicle CAN Network Bus           |
|                                                                                   |
+-----------------------------------------------------------------------------------+
""",
        "working_principle": "Hardware-Software Co-Design Paradigm:\nAn embedded system design is a continuous optimization between hardware and software. Tasks requiring nanosecond speed (e.g., CRC calculation, PWM pulse generation, edge timing) are implemented in dedicated silicon hardware peripherals, freeing the CPU core to execute high-level control algorithms without software polling loops.",
        "automotive_application": "Airbag Deployment Hard Real-Time ECU: A MEMS capacitive accelerometer detects a 35g vehicle deceleration. Within 2 ms, the embedded microcontroller reads the sensor via SPI, executes the crash discrimination algorithm, authenticates safety interlocks, and fires the high-current MOSFET squib drivers to inflate the driver airbag at exactly $t = 15\\text{ ms}$, saving the occupant before head-steering impact.",
        "comparison_table": {
            "headers": ["Characteristic", "General-Purpose Computer (PC)", "Automotive Embedded System (ECU)"],
            "rows": [
                ["System Goal", "Multiple user applications (Word, web, games)", "Single dedicated control function (e.g., ABS, BMS)"],
                ["Real-Time Constraint", "Non-real-time (Delay = minor annoyance)", "Hard real-time (Delay = fatal catastrophe)"],
                ["Operating System", "General OS (Windows, macOS, Ubuntu)", "Bare-Metal / RTOS (FreeRTOS, AUTOSAR Classic)"],
                ["Hardware Architecture", "CPU + External Chipset + Motherboard", "Single-chip Microcontroller (MCU) / SoC"],
                ["Power & Environment", "100W – 500W, cooled indoor office", "1W – 10W, automotive rated (-40°C to +125°C)"]
            ]
        },
        "formulas": [
            {
                "name": "Real-Time Schedulability Test (Rate Monotonic)",
                "math": "U = \\sum_{i=1}^{n} \\frac{C_i}{T_i} \\le n \\left( 2^{1/n} - 1 \\right) \\quad (\\lim_{n \\to \\infty} U = \\ln 2 \\approx 0.693)",
                "vars": [
                    "n = Total number of periodic tasks running in the embedded system",
                    "C_i = Worst-case execution time (WCET) of task i",
                    "T_i = Period / deadline of task i",
                    "U = Total CPU utilization"
                ],
                "example": "For 3 tasks with C1=1ms, T1=5ms (U1=0.2); C2=2ms, T2=10ms (U2=0.2); C3=3ms, T3=20ms (U3=0.15). Total U = 0.2 + 0.2 + 0.15 = 0.55. Since 0.55 <= 3*(2^(1/3) - 1) = 0.779, the system is mathematically guaranteed to meet 100% of hard real-time deadlines."
            }
        ],
        "code_snippet": """// Bare-Metal Infinite Embedded Control Loop Structure
#include "S32K144.h"

int main(void) {
    // 1. Hardware Initialization (Clocks, Watchdog, Pins)
    hardware_init();
    
    // 2. Peripheral Driver Setup (ADC, Timers, CAN)
    peripherals_init();
    
    // 3. Enable Global Interrupts (NVIC)
    __enable_irq();
    
    // 4. Super-Loop (Deterministic Reactive Control)
    while (1) {
        if (g_sensor_data_ready) {
            process_control_algorithm();
            update_actuators();
            g_sensor_data_ready = 0;
        }
        // Enter low-power sleep mode until next timer/sensor interrupt
        __WFI(); // Wait For Interrupt
    }
}""",
        "must_remember": [
            "Embedded systems are purpose-built, resource-constrained, and reactive to real-time events.",
            "Hard Real-Time: A missed deadline causes catastrophic system failure.",
            "Microcontrollers integrate CPU core, Flash, SRAM, and peripherals on a single silicon die.",
            "Rate Monotonic bound: U <= ln(2) ≈ 69.3% for guaranteed schedulability."
        ],
        "short_qa": [
            ("What is the difference between a Hard Real-Time system and a Soft Real-Time system?", "In a Hard Real-Time system, missing a single deadline results in total system failure and potential loss of life (e.g., airbag firing, ABS braking). In a Soft Real-Time system, missing a deadline only degrades performance or user experience without causing damage (e.g., multimedia audio playback)."),
            ("What are the primary hardware components integrated inside a single-chip microcontroller?", "Processor CPU core, non-volatile Program Memory (Flash/ROM), volatile Data Memory (SRAM), Clock Generators, Interrupt Controller, and I/O Peripherals (GPIO, Timers, ADC, UART, SPI, I2C, CAN).")
        ],
        "long_qa": [
            ("Define an Embedded System. Explain its structural building blocks and classify embedded systems based on real-time performance and architectural generations with automotive examples.", "A complete answer covers: (1) Formal definition; (2) Block diagram of host system, MCU, sensors, actuators, and communication buses; (3) Hard, Firm, and Soft real-time definitions; (4) Classification across 1st to 4th generations (8-bit to 32-bit multicore); (5) Rate Monotonic CPU schedulability formula; (6) Real automotive case study (airbag ECU).")
        ],
        "viva_interview_qa": [
            ("Why is the assembly instruction `__WFI()` (Wait For Interrupt) placed inside the main super-loop of an automotive microcontroller?", "`__WFI()` suspends core instruction execution and powers down internal CPU clock trees while keeping peripherals and timers active. The CPU draws near-zero current until a hardware event or periodic timer interrupt occurs, drastically reducing vehicle battery drain and operating temperatures.")
        ],
        "common_mistakes": [
            "Confusing high computational speed with real-time performance. A real-time system is not necessarily fast; it is **deterministic** (guarantees a bounded response time every single time).",
            "Writing `while(1)` loops with software delay loops in hard real-time systems. Software delay loops waste 100% of CPU cycles; hardware timers with interrupts must always be used."
        ],
        "revision_points": [
            "Embedded = Dedicated function + Real-time constraints.",
            "Hard Real-Time = Zero deadline tolerance (Airbags, Brakes).",
            "MCU = CPU + Flash + RAM + Peripherals on 1 chip.",
            "Super-loop + Interrupts = Standard bare-metal architecture."
        ],
        "sources": "Embedded System Design Lecture 1 Transcript; Course Syllabus Section 1 & 2 (Introduction to Embedded Systems)."
    },
    {
        "slug": "microprocessor-vs-microcontroller-architectures",
        "title": "Microprocessor vs Microcontroller & Processor Architectures",
        "module": "Embedded Fundamentals",
        "level": "Beginner",
        "importance": 5,
        "overview": "The selection between a Microprocessor (MPU) and a Microcontroller (MCU) represents the fundamental architectural division in computer engineering. Microprocessors feature high-speed processing cores that rely on external memory and peripherals, whereas Microcontrollers integrate CPU, memory, and rich I/O peripherals onto a single silicon chip for dedicated embedded control.",
        "learning_objectives": [
            "Compare the architectural differences between Microprocessors (MPU) and Microcontrollers (MCU).",
            "Contrast Von Neumann vs Harvard Memory Architectures.",
            "Analyze CISC (Complex Instruction Set Computer) vs RISC (Reduced Instruction Set Computer) design philosophies.",
            "Understand why automotive control systems exclusively use RISC Harvard microcontrollers (e.g., ARM Cortex-M4)."
        ],
        "prerequisites": "Embedded Systems Foundations, basic computer organization.",
        "core_concept": "Think of a Microprocessor as a high-powered race car engine sitting on a workbench: it has immense horsepower, but it cannot move until you separately wire up a fuel tank (RAM), transmission (chipset), dashboard (peripherals), and cooling system on a complex printed circuit board. A Microcontroller is a compact, self-contained go-kart: everything—engine, fuel tank, wheels, and steering—is built onto a single integrated chassis ready to drive immediately.",
        "lecture_notes": "Lecture 2 and 3 covered Microprocessors vs Microcontrollers, CISC vs RISC, and Harvard vs Von Neumann architectures. Prof. S. S. Kendre highlighted: 'In an MPU like Intel x86, the silicon die contains only the CPU; RAM, ROM, timers, and I/O are external on the motherboard. In an MCU like S32K144, CPU, Flash, SRAM, ADC, Timers, and CAN controllers are all fabricated on the same silicon die.' The professor demonstrated why Harvard architecture allows simultaneous instruction fetching and data reading in a single clock cycle.",
        "extra_explanation": "Let's analyze the two major architectural divisions:\n\n1. **Memory Architecture: Von Neumann vs Harvard:**\n   - **Von Neumann Architecture (Unified Memory):** Uses a single shared bus for both program instructions and data. **Von Neumann Bottleneck:** The CPU cannot read an instruction and read/write data memory at the same time because they share the same physical address/data bus.\n   - **Harvard Architecture (Separated Memory):** Uses physically separate memory blocks and distinct bus systems for instructions (Code Bus) and data (Data Bus). The CPU can fetch the next instruction while simultaneously reading or writing a data operand in SRAM in the exact same clock cycle.\n\n2. **Instruction Set Philosophy: CISC vs RISC:**\n   - **CISC (Complex Instruction Set Computer, e.g., x86):** Large instruction set (hundreds of instructions), variable instruction length (1 to 15 bytes), complex multi-cycle instructions, operations execute directly on memory operands.\n   - **RISC (Reduced Instruction Set Computer, e.g., ARM Cortex-M):** Small optimized instruction set, fixed instruction length (16/32-bit Thumb-2), single-cycle execution for most instructions, **Load-Store Architecture** (ALU operations execute strictly between registers; memory is accessed ONLY via `LDR` and `STR` instructions).",
        "workflow_steps": [
            ("Instruction Fetch (I-Code Bus)", "Core fetches 32-bit opcode from Flash memory over I-Bus"),
            ("Simultaneous Data Access (D-Code Bus)", "Core loads/stores SRAM variable over D-Bus in same cycle"),
            ("Instruction Decode", "Hardware decoder translates opcode into control signals"),
            ("ALU Register Execution", "RISC arithmetic executes in single cycle between R0-R12"),
            ("Result Writeback", "Calculated value latched into destination register")
        ],
        "diagram_ascii": """
+-----------------------------------------------------------------------------------+
|               VON NEUMANN VS HARVARD MEMORY ARCHITECTURES                         |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|    1. VON NEUMANN ARCHITECTURE (Shared Bus - Sequential Bottleneck)               |
|       +----------+                 Shared Address & Data Bus       +------------+ |
|       |   CPU    |<===============================================>| Unified    | |
|       |   Core   |                                                 | Memory     | |
|       +----------+                                                 | (Code+Data)| |
|                                                                    +------------+ |
|                                                                                   |
|    2. HARVARD ARCHITECTURE (ARM Cortex-M4 - Parallel High-Speed Buses)            |
|                      +------------------+                                         |
|                      |  Program Flash   | (Instructions)                          |
|                      +--------+---------+                                         |
|                               | (Dedicated I-Code Bus)                            |
|                               v                                                   |
|                        +--------------+                                           |
|                        |  ARM Cortex  |                                           |
|                        |   M4 Core    |                                           |
|                        +-------+------+                                           |
|                                ^                                                  |
|                                | (Dedicated D-Code / System Bus)                  |
|                      +--------+---------+                                         |
|                      |   Data SRAM /    | (Variables & Peripherals)               |
|                      |   Peripherals    |                                         |
|                      +------------------+                                         |
|                                                                                   |
+-----------------------------------------------------------------------------------+
""",
        "working_principle": "Why Automotive Control Systems Require RISC Harvard MCUs:\n1. **Deterministic Timing:** In RISC architectures, nearly all instructions take a predictable fixed number of clock cycles (typically 1 cycle), making worst-case execution time (WCET) mathematically provable.\n2. **Zero Bus Contention:** Harvard separate instruction and data buses prevent memory access stalls during high-frequency sensor sampling.\n3. **Low Power & High Reliability:** Single-chip integration eliminates high-capacitance external board traces, cutting electromagnetic emissions (EMC) and power consumption to milliwatts.",
        "automotive_application": "Powertrain Engine Control Module (ECM): An ECM microcontroller must calculate spark timing within 1 microsecond at 6000 RPM. Using an ARM Cortex-M4 RISC Harvard MCU, the CPU fetches the next lookup table interpolation instruction from Flash over the I-Code bus while simultaneously reading crankshaft sensor angle from SRAM over the D-Code bus, executing the spark advance calculation with zero bus wait states.",
        "comparison_table": {
            "headers": ["Architectural Parameter", "Microprocessor (MPU)", "Microcontroller (MCU)"],
            "rows": [
                ["Silicon Integration", "CPU Core only (External RAM/ROM/Peripherals)", "CPU + Flash + SRAM + Timers + ADC + CAN on 1 die"],
                ["System Cost & PCB Size", "Higher cost, large multi-layer PCB required", "Low cost, compact minimal component PCB"],
                ["Memory Architecture", "Predominantly Von Neumann unified caching", "Modified Harvard with separate Code & Data buses"],
                ["Instruction Set Philosophy", "CISC (x86) or High-end RISC (ARM Cortex-A)", "Strict Load-Store RISC (ARM Cortex-M)"],
                ["Power Consumption", "High (15W – 150W, requires active heat sinks)", "Ultra-low (0.05W – 2W, passive cooling)"],
                ["Primary Application", "Desktop, servers, infotainment screens", "Engine control, braking, body electronics, BMS"]
            ]
        },
        "formulas": [
            {
                "name": "Processor Instruction Execution Time",
                "math": "T_{exec} = \\frac{\\text{Instruction Count} \\times \\text{Average CPI}}{f_{clock}}",
                "vars": [
                    "Instruction Count = Total number of assembly instructions in algorithm",
                    "CPI = Clock Cycles Per Instruction (Average ~1.2 for RISC Cortex-M4)",
                    "f_clock = Processor operating clock frequency (Hz, e.g., 80 MHz for S32K144)"
                ],
                "example": "An ABS control loop contains 400 RISC instructions with average CPI = 1.25 running on an 80 MHz clock. Execution time is T_exec = (400 × 1.25) / (80 × 10^6) = 500 / 80,000,000 = 6.25 μs."
            }
        ],
        "code_snippet": """// RISC Load-Store Architecture vs CISC Assembly Comparison
// In ARM Cortex-M (RISC): Memory CANNOT be added directly!
// You must explicitly LOAD into registers, ADD, and STORE back:
LDR  R0, =sensor_val1    // Load address of sensor 1
LDR  R1, [R0]            // Load value of sensor 1 into Register R1
LDR  R2, =sensor_val2    // Load address of sensor 2
LDR  R3, [R2]            // Load value of sensor 2 into Register R3
ADD  R4, R1, R3          // ALU executes addition between registers (1 cycle!)
LDR  R5, =result         // Load address of result
STR  R4, [R5]            // Store register value back into SRAM memory""",
        "must_remember": [
            "MCU integrates CPU, Flash, SRAM, and I/O peripherals onto a single silicon chip.",
            "MPU contains only CPU; requires external RAM, ROM, and chipset on motherboard.",
            "Harvard Architecture has separate instruction and data buses, eliminating Von Neumann bottleneck.",
            "RISC uses fixed-length instructions and strict Load-Store architecture (operations only on registers)."
        ],
        "short_qa": [
            ("What is the Von Neumann Bottleneck?", "In Von Neumann architecture, a single shared bus connects the CPU to unified memory. The CPU cannot fetch an instruction and read/write a data variable at the same time, causing the memory bus throughput to become the primary speed bottleneck."),
            ("What is meant by a 'Load-Store' architecture in RISC processors?", "In a Load-Store architecture (such as ARM Cortex-M), arithmetic and logic instructions (like ADD, SUB, AND) can operate ONLY on internal CPU registers, never directly on memory. Memory is accessed strictly through dedicated Load (`LDR`) and Store (`STR`) instructions.")
        ],
        "long_qa": [
            ("Compare Microprocessors and Microcontrollers across hardware integration, memory architecture (Von Neumann vs Harvard), instruction sets (CISC vs RISC), and power consumption. Explain why automotive real-time ECUs are built using RISC Harvard microcontrollers.", "A complete answer covers: (1) Hardware integration comparison table; (2) Block diagrams of Von Neumann vs Harvard memory systems; (3) Explanation of the Von Neumann bottleneck; (4) Detailed comparison of CISC vs RISC with assembly examples; (5) Explanation of why automotive ECUs demand RISC Harvard microcontrollers (deterministic timing, single-cycle execution, low EMC, and single-chip reliability).")
        ],
        "viva_interview_qa": [
            ("Why is the ARM Cortex-M4 processor described as a 'Modified Harvard' architecture rather than a pure Harvard architecture?", "A pure Harvard architecture has completely isolated physical address spaces for program and data. ARM Cortex-M4 uses a unified 4 GB memory address map where Code, SRAM, and Peripherals share address space, but accesses them over **separate, parallel physical buses** (I-Code, D-Code, System Bus), allowing parallel access while maintaining unified C pointer compatibility.")
        ],
        "common_mistakes": [
            "Assuming RISC is 'slower' because it has fewer instructions. RISC executes simpler instructions in single clock cycles at much higher clock frequencies, outperforming CISC in real-time control.",
            "Confusing 32-bit architecture with clock speed. A 32-bit architecture means the internal registers, ALU data path, and memory bus widths are 32 bits wide."
        ],
        "revision_points": [
            "MCU = All-in-one chip (CPU + Flash + RAM + I/O).",
            "MPU = CPU only (External RAM/ROM).",
            "Harvard = Separate Code & Data buses (Parallel access).",
            "RISC = Fixed length, single-cycle, Load-Store only."
        ],
        "sources": "Embedded System Design Lecture 2 & 3 Transcripts; Course Syllabus Section 2 (Microprocessor Vs Microcontroller, CISC vs RISC)."
    },
    {
        "slug": "arm-cortex-m4-core-architecture",
        "title": "ARM Cortex-M4 Core Architecture & Bus Matrix",
        "module": "Processor Architecture",
        "level": "Intermediate",
        "importance": 5,
        "overview": "The ARM Cortex-M4 is an industry-standard 32-bit RISC processor core engineered specifically for deterministic, high-performance, cost-sensitive real-time embedded control applications. Featuring a 3-stage instruction pipeline, Harvard bus architecture, Single Instruction Multiple Data (SIMD) capabilities, hardware divide, single-cycle Multiply-Accumulate (MAC), and an optional IEEE 754 Floating Point Unit (FPU), the Cortex-M4 forms the computational heart of automotive microcontrollers such as the NXP S32K144.",
        "learning_objectives": [
            "Analyze the internal architecture of the ARM Cortex-M4 32-bit RISC core.",
            "Explain the operation of the 3-stage instruction pipeline (Fetch, Decode, Execute).",
            "Understand the multi-layer AHB-Lite Bus Matrix and its interconnected master/slave ports.",
            "Differentiate between I-Code, D-Code, System (S-Bus), and Private Peripheral Bus (PPB)."
        ],
        "prerequisites": "Microprocessor vs Microcontroller, Harvard Architecture fundamentals.",
        "core_concept": "To execute instructions at 80 to 120 MHz without memory bottlenecks, the Cortex-M4 core does not execute one instruction start-to-finish before starting the next. It uses an assembly-line approach called a **3-stage pipeline**: while Instruction 3 is being fetched from Flash, Instruction 2 is being decoded, and Instruction 1 is actively executing in the ALU. Under steady-state conditions, one instruction completes on every single clock cycle (1 CPI).",
        "lecture_notes": "Lecture 1, 3, and 5 of Embedded System Design detailed the ARM Cortex-M4 processor architecture. Prof. S. S. Kendre explained: 'The Cortex-M4 core is a 32-bit architecture with a Harvard bus matrix. It features three external Advanced High-performance Bus (AHB-Lite) interfaces: I-Code for instruction fetches from Flash, D-Code for constant data reads from Flash, and System Bus for SRAM and peripherals.' The professor highlighted the hardware DSP instructions and single-cycle MAC unit, which allow digital filtering and motor vector control algorithms to run in real-time.",
        "extra_explanation": "Let's analyze the core architectural blocks:\n\n1. **3-Stage Pipeline (Fetch, Decode, Execute):**\n   - **Fetch:** The instruction is retrieved from memory at the address pointed to by the Program Counter (PC).\n   - **Decode:** The instruction is identified by the instruction decoder, generating control signals for the datapath and register bank.\n   - **Execute:** The ALU or hardware multiplier processes register operands and writes back results.\n   - *Pipeline Flush:* When a branch instruction (e.g., `B`, `BL`, `BX`) is taken, the pre-fetched instructions in the pipeline become invalid and must be flushed, causing a 2 to 3 cycle branch penalty.\n\n2. **Multi-Layer AHB-Lite Bus Matrix:**\n   - The Cortex-M4 communicates with memory and peripherals through distinct physical 32-bit buses:\n     - **I-Code Bus (Instruction Code):** Connects the core to the Flash memory controller strictly for instruction fetches ($0\\text{x}00000000$ to $0\\text{x}1FFFFFFF$).\n     - **D-Code Bus (Data Code):** Connects the core to Flash for literal and constant data table reads.\n     - **System Bus (S-Bus):** Connects the core to SRAM memory ($0\\text{x}20000000$) and on-chip peripherals ($0\\text{x}40000000$).\n     - **Private Peripheral Bus (PPB):** Connects directly to internal core peripherals: Nested Vectored Interrupt Controller (NVIC), SysTick Timer, Memory Protection Unit (MPU), and Core Debug modules ($0\\text{xE}0000000$).",
        "workflow_steps": [
            ("Cycle N: Fetch", "I-Code bus fetches Instruction 3 from Flash at address [PC]"),
            ("Cycle N: Decode", "Instruction decoder decodes opcode of Instruction 2"),
            ("Cycle N: Execute", "ALU executes arithmetic of Instruction 1 between registers"),
            ("Cycle N+1: Pipeline Advance", "Instruction 1 completes; Instruction 2 executes; Instruction 4 fetched"),
            ("Branch Execution (if taken)", "If branch taken, pipeline is flushed; PC reloads new target address")
        ],
        "diagram_ascii": """
+-----------------------------------------------------------------------------------+
|               ARM CORTEX-M4 INTERNAL ARCHITECTURE & BUS MATRIX                    |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|  +-----------------------------------------------------------------------------+  |
|  |                           ARM CORTEX-M4 CORE                                |  |
|  |                                                                             |  |
|  |  +-----------------------+     +-----------------------+     +-----------+  |  |
|  |  | Register Bank (R0-R15)|<===>| 32-bit ALU / MAC Unit |<===>|   FPU     |  |  |
|  |  | (MSP, PSP, CONTROL)   |     | (Single-Cycle Mult)   |     |(Hardware) |  |  |
|  |  +-----------------------+     +-----------------------+     +-----------+  |  |
|  |              ^                             ^                                |  |
|  |              |                             |                                |  |
|  |  +-----------+-----------------------------+-----------+                    |  |
|  |  |  3-STAGE PIPELINE :  [ FETCH ] -> [ DECODE ] -> [ EXECUTE ]              |  |
|  |  +-----------------------------------------------------+                    |  |
|  +-------------------------------------+---------------------------------------+  |
|                                        |                                          |
|            +---------------------------+---------------------------+              |
|            |                           |                           |              |
|            v (I-Code Bus)              v (D-Code Bus)              v (System Bus) |
|     +--------------+            +--------------+            +--------------+      |
|     | Flash Memory |            | Constant Data|            | SRAM Memory  |      |
|     | Instructions |            | Tables (ROM) |            | & Peripherals|      |
|     +--------------+            +--------------+            +--------------+      |
|                                                                                   |
|            +-------------------------------------------------------+              |
|            v (Private Peripheral Bus - PPB)                                       |
|     +--------------+------------+------------+------------+                       |
|     |  NVIC Ctrl   |  SysTick   |    MPU     | Core Debug |                       |
|     +--------------+------------+------------+------------+                       |
|                                                                                   |
+-----------------------------------------------------------------------------------+
""",
        "working_principle": "Single-Cycle Multiply-Accumulate (MAC) & DSP Engine:\nThe Cortex-M4 includes dedicated hardware multiplier blocks capable of calculating a 32-bit by 32-bit multiplication with 64-bit accumulation ($R_d = R_a + (R_m \\times R_n)$) in a **single clock cycle**. This hardware acceleration enables the microcontroller to execute complex Finite Impulse Response (FIR) digital filters and Clarke/Park vector transformations for electric vehicle motor control without needing a separate DSP chip.",
        "automotive_application": "Field Oriented Control (FOC) of EV Traction Motor: In an electric vehicle traction inverter, the MCU must calculate the 3-phase currents ($i_a, i_b, i_c$), execute Clarke and Park matrix coordinate transformations, run two PI current loops, and compute Space Vector PWM (SVPWM) timings. The Cortex-M4 hardware FPU and single-cycle MAC compute the entire FOC algorithm in under $12\\ \\mu\\text{s}$, leaving 88% of CPU bandwidth free for vehicle communications.",
        "comparison_table": {
            "headers": ["ARM Cortex-M Core", "Architecture", "Pipeline", "Hardware FPU", "DSP / SIMD Instructions", "Target Automotive Domain"],
            "rows": [
                ["Cortex-M0+", "ARMv6-M (Von Neumann)", "2-Stage", "No", "No", "Simple door nodes, window lifters, lighting"],
                ["Cortex-M3", "ARMv3-M (Harvard)", "3-Stage", "No", "No (Hardware divide only)", "Body control, climate, basic instrument clusters"],
                ["Cortex-M4", "ARMv7E-M (Harvard)", "3-Stage", "Optional (Single Precision)", "Yes (Single-cycle MAC & SIMD)", "Powertrain ECM, EV Motor Inverter, ABS/ESP, Gateway"],
                ["Cortex-M7", "ARMv7E-M (Dual-Issue)", "6-Stage", "Single & Double Precision", "Yes (High-performance DSP)", "Advanced Gateway, Digital Cockpit, ADAS Radar"]
            ]
        },
        "formulas": [
            {
                "name": "Pipeline Throughput and Branch Penalty Calculation",
                "math": "\\text{Total Cycles} = N_{inst} + N_{branches} \\times (P_{depth} - 1)",
                "vars": [
                    "N_inst = Total number of linear assembly instructions executed",
                    "N_branches = Number of branch instructions taken",
                    "P_depth = Pipeline depth (3 for ARM Cortex-M4)"
                ],
                "example": "A loop contains 20 instructions and executes 100 iterations (total 2000 instructions) with 100 taken branch instructions. Total clock cycles = 2000 + 100 × (3 - 1) = 2000 + 200 = 2200 cycles (Average CPI = 1.10)."
            }
        ],
        "code_snippet": """// CMSIS Hardware DSP Multiply-Accumulate Example on Cortex-M4
#include "arm_math.h"

// Calculate dot product (FIR Filter Step): y = sum(x[i] * h[i])
float32_t calculate_fir_tap(const float32_t* x, const float32_t* h, uint32_t num_taps) {
    float32_t result = 0.0f;
    // Uses single-cycle hardware floating-point MAC instructions (VMLA.F32)
    arm_dot_prod_f32(x, h, num_taps, &result);
    return result;
}""",
        "must_remember": [
            "ARM Cortex-M4 is a 32-bit RISC core with a 3-stage pipeline (Fetch, Decode, Execute).",
            "Harvard Bus Matrix has separate I-Code, D-Code, System (S-Bus), and PPB buses.",
            "Includes hardware divide, single-cycle MAC, and optional single-precision FPU.",
            "Private Peripheral Bus (PPB) connects directly to NVIC, SysTick, and Core Debug modules."
        ],
        "short_qa": [
            ("What are the four primary external buses in the ARM Cortex-M4 bus matrix?", "I-Code Bus (Instruction fetches from Flash), D-Code Bus (Literal/data reads from Flash), System Bus (SRAM and peripheral access), and Private Peripheral Bus / PPB (Internal core registers: NVIC, SysTick, MPU)."),
            ("What happens inside the Cortex-M4 3-stage pipeline when a branch instruction is taken?", "When a branch is taken, the instructions already present in the Fetch and Decode stages are invalid. The pipeline is flushed (cleared), causing a 2-cycle branch penalty while the new instruction address is fetched into the pipeline.")
        ],
        "long_qa": [
            ("Explain the internal core architecture of the ARM Cortex-M4 processor. Describe the 3-stage instruction pipeline, the multi-layer AHB-Lite bus matrix, and the hardware DSP/FPU capabilities with an architectural block diagram.", "A complete answer covers: (1) Architectural block diagram showing core, register bank, ALU, FPU, and memory interfaces; (2) Detailed explanation of Fetch, Decode, and Execute pipeline stages; (3) Detailed description of I-Code, D-Code, System, and PPB buses; (4) Hardware DSP features (single-cycle MAC, SIMD instructions, hardware divide); (5) Pipeline branch penalty calculation.")
        ],
        "viva_interview_qa": [
            ("Why does the Cortex-M4 separate the I-Code bus and D-Code bus if both connect to the same Flash memory controller?", "Separating I-Code and D-Code allows the Flash controller's internal arbiter to serve simultaneous instruction fetches and literal constant reads through a pipelined prefetch buffer, eliminating CPU execution stalls when reading calibration look-up tables from Flash.")
        ],
        "common_mistakes": [
            "Assuming Cortex-M4 has a 5-stage pipeline. The Cortex-M4 has a **3-stage pipeline** (Fetch, Decode, Execute). Cortex-M7 has a 6-stage pipeline.",
            "Confusing Cortex-M (Microcontroller real-time profile) with Cortex-A (Application profile running Android/Linux) or Cortex-R (Real-time safety with dual-core lockstep)."
        ],
        "revision_points": [
            "Cortex-M4 = 32-bit RISC, 3-Stage Pipeline, Harvard Buses.",
            "Buses: I-Code (Code), D-Code (Constants), System (SRAM/Peripherals), PPB (NVIC).",
            "Single-cycle MAC + Hardware FPU.",
            "Target: Automotive Powertrain, Inverters, Gateway, Chassis."
        ],
        "sources": "Embedded System Design Lecture 1 & 5 Transcripts; ARM Cortex-M4 Processor Technical Reference Manual; Course Syllabus Section 3."
    },
    {
        "slug": "arm-cortex-m4-programmers-model",
        "title": "ARM Cortex-M4 Programmer's Model & Register Set",
        "module": "Processor Architecture",
        "level": "Intermediate",
        "importance": 5,
        "overview": "The programmer's model defines the register set, operating modes, privilege levels, and execution states visible to software running on the ARM Cortex-M4 core. Mastering the 16 core 32-bit registers (R0 to R15), dual stack pointers (MSP and PSP), Special Function Registers (xPSR, CONTROL, PRIMASK), and the distinction between Thread Mode and Handler Mode is essential for embedded C and assembly programming.",
        "learning_objectives": [
            "Identify and analyze all 16 core 32-bit registers: General Purpose (R0-R12), SP (R13), LR (R14), and PC (R15).",
            "Differentiate between the dual banked Stack Pointers: Main Stack Pointer (MSP) vs Process Stack Pointer (PSP).",
            "Analyze the Program Status Register (xPSR: APSR, IPSR, and EPSR fields).",
            "Explain Processor Operating Modes (Thread vs Handler Mode) and Privilege Levels (Privileged vs Unprivileged)."
        ],
        "prerequisites": "ARM Cortex-M4 Core Architecture, basic register concepts.",
        "core_concept": "To prevent a bug in user software from crashing the entire vehicle operating system, the Cortex-M4 separates software into two worlds: **Thread Mode** (where normal application tasks run, optionally restricted to unprivileged access) and **Handler Mode** (which enters automatically whenever an interrupt/exception occurs, always with full privileged access). It also provides two separate stacks (MSP for the OS/interrupts and PSP for application tasks) so that an application stack overflow cannot corrupt interrupt execution.",
        "lecture_notes": "Lecture 3 and 4 covered the Programmer's Model and Register Set in detail. Prof. S. S. Kendre explained: 'The Cortex-M4 has 16 core registers R0 to R15. R0 to R12 are general purpose. R13 is the Stack Pointer. But look closely: R13 is banked into two physical registers—MSP and PSP. Only one is active at a time, selected by the CONTROL register.' The professor walked through the xPSR register, showing how the condition flags (N, Z, C, V) in APSR are updated by arithmetic instructions and checked by conditional branches.",
        "extra_explanation": "Let's analyze the **Register Organization & Special Registers**:\n\n1. **Core Register Set (32-bit each):**\n   - **R0 to R12 (General Purpose):** R0-R7 are 'Low Registers' (accessible by all 16-bit and 32-bit Thumb-2 instructions); R8-R12 are 'High Registers' (accessible by all 32-bit instructions). Under the ARM Architecture Procedure Call Standard (AAPCS), **R0-R3** pass input parameters to C functions and return function results; **R4-R11** must be preserved across function calls.\n   - **R13 (Stack Pointer - SP):** Banked into two registers:\n     - **MSP (Main Stack Pointer):** Used by default after reset and always used by Exception Handlers (Handler Mode).\n     - **PSP (Process Stack Pointer):** Used by application tasks in Thread Mode under an RTOS (e.g., FreeRTOS).\n   - **R14 (Link Register - LR):** Holds the return address when calling a subroutine (`BL`) or an `EXC_RETURN` code during exception entry.\n   - **R15 (Program Counter - PC):** Points to the current instruction address $+4$ bytes (due to pipeline prefetch). Bit 0 is always 0 because instructions are halfword-aligned; executing code must have LSB=1 to indicate Thumb state.\n\n2. **Program Status Register (xPSR):**\n   - **APSR (Application PSR):** Bits 31-28 contain ALU condition flags: **N** (Negative), **Z** (Zero), **C** (Carry), **V** (Overflow), and **Q** (Saturation).\n   - **IPSR (Interrupt PSR):** Bits 8-0 hold the active Exception Number (0 = Thread mode, 15 = SysTick, 16+ = External IRQ).\n   - **EPSR (Execution PSR):** Contains the **T-bit** (Bit 24, Thumb state = 1; clearing causes a HardFault) and ICI/IT execution state bits.\n\n3. **Special Control Registers (Accessed via `MRS` / `MSR`):**\n   - **CONTROL Register:** Bit 0 selects Privileged (0) vs Unprivileged (1) access; Bit 1 selects active stack pointer (0 = MSP, 1 = PSP).\n   - **PRIMASK Register:** 1-bit register; writing 1 disables all maskable interrupts (`__disable_irq()`).",
        "workflow_steps": [
            ("Power-On Reset", "CPU boots into Thread Mode with Privileged Access using MSP"),
            ("RTOS Initialization", "RTOS configures application tasks to run in Thread Mode using PSP"),
            ("Interrupt Event", "Hardware interrupt occurs (e.g., CAN message received)"),
            ("Automatic Mode Switch", "CPU switches automatically to Handler Mode (Privileged, MSP)"),
            ("ISR Return", "CPU executes BX LR with EXC_RETURN; restores Thread Mode & PSP")
        ],
        "diagram_ascii": """
+-----------------------------------------------------------------------------------+
|               ARM CORTEX-M4 PROGRAMMER'S MODEL & REGISTER SET                      |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|  GENERAL PURPOSE REGISTERS                                                        |
|  +--------------------+---------------------------------------------------------+ |
|  | R0  to  R7         | Low Registers (Accessible by all Thumb instructions)    | |
|  | (R0-R3 = Params)   | R0-R3 hold C function arguments & return values         | |
|  +--------------------+---------------------------------------------------------+ |
|  | R8  to  R12        | High Registers (General 32-bit computation)             | |
|  +--------------------+---------------------------------------------------------+ |
|                                                                                   |
|  SPECIAL CORE REGISTERS                                                           |
|  +--------------------+------------------+--------------------------------------+ |
|  | R13 (SP)           | Main SP (MSP)    | Used by OS & All Interrupt Handlers  | |
|  | (Banked Dual SP)   | Process SP (PSP) | Used by Application Tasks in Thread  | |
|  +--------------------+------------------+--------------------------------------+ |
|  | R14 (LR)           | Link Register    | Holds subroutine return / EXC_RETURN | |
|  +--------------------+------------------+--------------------------------------+ |
|  | R15 (PC)           | Program Counter  | Holds current instruction address    | |
|  +--------------------+------------------+--------------------------------------+ |
|                                                                                   |
|  PROGRAM STATUS REGISTER (xPSR)                                                   |
|  +----+----+----+----+----+---------------------+--------+----------------------+ |
|  | N  | Z  | C  | V  | Q  |      RESERVED       |   T    |  IPSR (Exception #)  | |
|  +----+----+----+----+----+---------------------+--------+----------------------+ |
|  | 31 | 30 | 29 | 28 | 27 |      26 to 25       |   24   |      8 to 0          | |
|  |<---- APSR (Flags) ---->|                     |(Thumb=1)|<-- Active ISR # ---->| |
|                                                                                   |
+-----------------------------------------------------------------------------------+
""",
        "working_principle": "Operating Modes vs Privilege Levels Matrix:\n- **Thread Mode + Privileged:** Operating state immediately after chip reset; used by RTOS kernel and bare-metal systems.\n- **Thread Mode + Unprivileged:** Used for sandboxed user application tasks; hardware restricts access to NVIC and system timers.\n- **Handler Mode + Always Privileged:** Operating state inside all Interrupt Service Routines (ISRs) and System Exception Handlers. Entered automatically via hardware when an interrupt fires.",
        "automotive_application": "AUTOSAR Memory Partitioning & Stack Isolation: In an automotive gateway ECU, safety-critical CAN routing tasks run using the Main Stack Pointer (MSP) in Privileged mode. Third-party infotainment and telematics apps run using the Process Stack Pointer (PSP) in Unprivileged mode. If the infotainment app crashes or suffers a stack overflow, the Memory Protection Unit (MPU) catches the violation without affecting the powertrain CAN tasks.",
        "comparison_table": {
            "headers": ["Operating Mode", "Privilege Level", "Active Stack Pointer", "Primary Purpose"],
            "rows": [
                ["Thread Mode (Reset)", "Privileged (CONTROL[0]=0)", "MSP (Main Stack Pointer)", "Bare-metal applications, RTOS Kernel startup"],
                ["Thread Mode (User Task)", "Unprivileged (CONTROL[0]=1)", "PSP (Process Stack Pointer)", "Isolated user tasks under FreeRTOS / AUTOSAR"],
                ["Handler Mode", "Privileged (Always)", "MSP (Always forced by hardware)", "All Interrupt Handlers (ISR), Fault Handlers, SysTick"]
            ]
        },
        "formulas": [
            {
                "name": "AAPCS Register Calling Convention Mapping",
                "math": "\\text{Inputs: } R0, R1, R2, R3 \\quad \\implies \\quad \\text{Return Value: } R0 \\text{ (or } R0:R1 \\text{ for 64-bit)}",
                "vars": [
                    "R0-R3 = Scratch registers used for passing up to four 32-bit arguments",
                    "R4-R11 = Callee-saved registers (must be pushed to stack if modified)",
                    "R12 (IP) = Intra-procedure scratch register",
                    "R14 (LR) = Holds return address"
                ],
                "example": "Calling a C function `uint32_t calculate_torque(uint16_t rpm, uint16_t pedal)` places `rpm` into R0 and `pedal` into R1 before executing `BL calculate_torque`. The calculated torque is returned in R0."
            }
        ],
        "code_snippet": """// Accessing Special Registers via Inline Assembly (ARM Cortex-M4)
#include <stdint.h>

void switch_to_user_mode(uint32_t psp_stack_address) {
    // 1. Set Process Stack Pointer (PSP) address
    __asm volatile ("MSR PSP, %0" : : "r" (psp_stack_address) : );
    
    // 2. Set CONTROL register: Bit 1 = 1 (Use PSP), Bit 0 = 1 (Unprivileged)
    __asm volatile ("MSR CONTROL, %0" : : "r" (0x03) : );
    
    // 3. Instruction Synchronization Barrier
    __asm volatile ("ISB");
}

uint32_t get_active_exception_number(void) {
    uint32_t ipsr_val;
    __asm volatile ("MRS %0, IPSR" : "=r" (ipsr_val) : : );
    return ipsr_val & 0x1FF; // Bits 8:0 hold active exception #
}""",
        "must_remember": [
            "16 core registers: R0-R12 (General), R13 (SP), R14 (LR), R15 (PC).",
            "R13 is banked into MSP (Main Stack) and PSP (Process Stack).",
            "Handler Mode is ALWAYS Privileged and ALWAYS uses MSP.",
            "Thread Mode is used for applications and can be Privileged or Unprivileged.",
            "xPSR contains APSR (ALU Flags N,Z,C,V), IPSR (Exception #), and EPSR (Thumb T-bit)."
        ],
        "short_qa": [
            ("What is the difference between the Main Stack Pointer (MSP) and the Process Stack Pointer (PSP)?", "MSP is the default stack pointer used upon reset and is ALWAYS used by all interrupt service routines in Handler Mode. PSP is an alternate stack pointer used exclusively by application tasks in Thread Mode under an RTOS to prevent task stack overflows from corrupting OS kernel and interrupt execution."),
            ("What are the two processor operating modes in ARM Cortex-M4?", "Thread Mode (used for executing normal background application software) and Handler Mode (entered automatically when executing interrupt handlers and system exceptions).")
        ],
        "long_qa": [
            ("Describe the complete Programmer's Model of the ARM Cortex-M4 processor. Detail the 16 core registers, the dual banked stack pointers, the xPSR register fields, and the transition between Thread Mode and Handler Mode.", "A complete answer covers: (1) Core register diagram (R0-R15); (2) AAPCS function calling convention for R0-R3; (3) Explanation of MSP vs PSP; (4) Detailed bit breakdown of xPSR (APSR condition flags, IPSR exception numbers, EPSR T-bit); (5) CONTROL register operation; (6) Mode transition diagram between Thread Mode and Handler Mode upon interrupt assertion.")
        ],
        "viva_interview_qa": [
            ("What fatal hardware fault occurs if software clears Bit 24 (the T-bit) in the EPSR register on an ARM Cortex-M4?", "The T-bit indicates Thumb state. Because the Cortex-M4 core supports ONLY the Thumb-2 instruction set (it does not possess an ARM 32-bit legacy execution state), clearing the T-bit to 0 causes the processor to attempt executing non-existent ARM state instructions, immediately triggering an unrecoverable **UsageFault / HardFault**.")
        ],
        "common_mistakes": [
            "Attempting to switch to PSP stack pointer inside an Interrupt Service Routine. Hardware forces MSP in Handler Mode; software cannot use PSP inside an ISR.",
            "Modifying R15 (PC) directly without setting bit 0 to 1. In Cortex-M, all branch target addresses loaded into PC must have bit 0 set to 1 to maintain Thumb execution state."
        ],
        "revision_points": [
            "R0-R12: General Purpose (R0-R3 = Function parameters).",
            "R13: Dual SP (MSP for OS/ISRs, PSP for Tasks).",
            "R14: Link Register (Return address / EXC_RETURN).",
            "R15: Program Counter (Holds instruction address + 4).",
            "Modes: Thread (App) vs Handler (ISR)."
        ],
        "sources": "Embedded System Design Lecture 3 & 4 Transcripts; The Definitive Guide to ARM Cortex-M3/M4 Processors (Joseph Yiu) Chapter 4; Course Syllabus Section 3."
    }
,
{'slug': 'arm-cortex-m4-nvic-and-exceptions',
 'title': 'Nested Vectored Interrupt Controller (NVIC) & Exception Handling',
 'module': 'Interrupts & Peripherals',
 'level': 'Intermediate',
 'importance': 5,
 'overview': 'Real-time automotive microcontrollers must respond instantaneously to asynchronous '
             'external events (such as CAN message reception, timer overflows, and ADC conversion '
             'completions). The ARM Cortex-M4 integrates the Nested Vectored Interrupt Controller '
             '(NVIC) tightly into the core pipeline, providing hardware-managed priority nesting, '
             'deterministic 12-cycle interrupt latency, automatic hardware context saving '
             '(stacking), Tail-Chaining, and Late-Arrival optimizations.',
 'learning_objectives': ['Analyze the ARM Cortex-M4 Exception Model: System Exceptions (Reset, '
                         'NMI, HardFault, SysTick) vs External Interrupts (IRQs).',
                         'Understand the Vector Table structure located at memory address '
                         '$0\\text{x}00000000$.',
                         'Explain NVIC hardware features: Priority grouping (Preemption vs '
                         'Sub-priority), Tail-Chaining (6-cycle switchover), and Late-Arrival '
                         'handling.',
                         'Trace the automatic hardware stacking and unstacking sequence (R0-R3, '
                         'R12, LR, PC, xPSR) during interrupt entry and exit.'],
 'prerequisites': "ARM Cortex-M4 Core Architecture, Programmer's Model & Registers, Stack Pointer "
                  '(MSP/PSP).',
 'core_concept': 'In older microcontrollers (like 8051 or ARM7), when an interrupt fired, software '
                 'had to execute dozens of assembly instructions to manually push registers to the '
                 'stack, identify the interrupt source, and jump to the handler, taking over 50 '
                 'clock cycles. In the Cortex-M4, the NVIC is built directly inside the CPU '
                 'silicon: the hardware automatically pushes registers to RAM and branches to the '
                 'exact ISR address in just **12 clock cycles**.',
 'lecture_notes': 'Lecture 4 and 5 of Embedded System Design covered the NVIC in detail. Prof. S. '
                  "S. Kendre highlighted: 'The NVIC is a vectored interrupt controller. Vectored "
                  'means the hardware fetches the exact function pointer from the Vector Table in '
                  "memory; there is zero software polling required!' The professor walked through "
                  'the 8-register hardware stacking frame (R0-R3, R12, LR, PC, xPSR) and explained '
                  'how Tail-Chaining saves 18 clock cycles when two interrupts occur back-to-back.',
 'extra_explanation': "Let's analyze the **Cortex-M4 Exception & NVIC Mechanics**:\n"
                      '\n'
                      '1. **The Vector Table ($0\\text{x}00000000$ to $0\\text{x}000001FF$):**\n'
                      '   - Vector 0 ($0\\text{x}00000000$): Initial Main Stack Pointer value '
                      '(Initial MSP).\n'
                      '   - Vector 1 ($0\\text{x}00000004$): Initial Program Counter (Reset '
                      'Handler address with LSB=1).\n'
                      '   - Vector 2 ($0\\text{x}00000008$): Non-Maskable Interrupt (NMI).\n'
                      '   - Vector 3 ($0\\text{x}0000000C$): HardFault Handler.\n'
                      '   - Vector 11 ($0\\text{x}0000002C$): SVCall (Supervisor Call for RTOS).\n'
                      '   - Vector 14 ($0\\text{x}00000038$): PendSV (Context Switch Handler for '
                      'RTOS).\n'
                      '   - Vector 15 ($0\\text{x}0000003C$): SysTick Timer Handler.\n'
                      '   - Vector 16+ ($0\\text{x}00000040$+): Microcontroller-specific '
                      'peripheral IRQs (GPIO, Timers, CAN, ADC).\n'
                      '\n'
                      '2. **Automatic Hardware Stacking Frame (Interrupt Entry):**\n'
                      '   - Upon IRQ assertion, the processor hardware automatically pushes **8 '
                      'registers** onto the current stack in descending order: `xPSR`, `PC` '
                      '(return address), `LR`, `R12`, `R3`, `R2`, `R1`, `R0`.\n'
                      '   - The CPU loads the Link Register (LR) with a special **`EXC_RETURN`** '
                      'value (e.g., $0\\text{xFFFFFFF9}$ to return to Thread mode using MSP, or '
                      '$0\\text{xFFFFFFFD}$ for Thread mode using PSP).\n'
                      '   - The CPU loads PC with the ISR address fetched from the Vector Table '
                      'and begins executing the ISR in Handler Mode in strictly **12 clock '
                      'cycles**.\n'
                      '\n'
                      '3. **NVIC Performance Optimizations:**\n'
                      '   - **Tail-Chaining:** When an ISR finishes and a second pending interrupt '
                      'exists, instead of unstacking 8 registers and immediately re-stacking them '
                      '(24 cycles wasted), the NVIC simply skips unstacking/restacking and '
                      'branches directly to the next ISR in **only 6 clock cycles**!\n'
                      '   - **Late-Arrival:** If a higher-priority interrupt arrives while the CPU '
                      'is in the middle of stacking registers for a lower-priority interrupt, the '
                      'NVIC dynamically switches to the higher-priority ISR without restarting the '
                      'stacking process.',
 'workflow_steps': [('Peripheral Event', 'CAN controller asserts interrupt line to NVIC'),
                    ('Priority Evaluation',
                     'NVIC checks if IRQ priority is higher than currently running task'),
                    ('Hardware Context Stacking',
                     'Core automatically pushes R0-R3, R12, LR, PC, xPSR onto stack in 12 cycles'),
                    ('Vector Fetch & Mode Switch',
                     'Core fetches ISR address from Vector Table; switches to Handler Mode'),
                    ('ISR Execution & EXC_RETURN',
                     'ISR clears interrupt flag; executes BX LR with EXC_RETURN; hardware unstacks '
                     'frame')],
 'diagram_ascii': '\n'
                  '+-----------------------------------------------------------------------------------+\n'
                  '|               ARM CORTEX-M4 HARDWARE INTERRUPT STACKING '
                  'FRAME                     |\n'
                  '+-----------------------------------------------------------------------------------+\n'
                  '|                                                                                   '
                  '|\n'
                  '|    Memory Address (Descending Stack - SP moves '
                  'down)                              |\n'
                  '|         '
                  '|                                                                         |\n'
                  '|         |   [ Previous Stack Content (Local variables / Call frames) '
                  ']            |\n'
                  '|         |   '
                  '+--------------------------------------------------------+            |\n'
                  '|         |   |  xPSR       (Program Status Register condition flags)  |  <-- '
                  'SP + 28|\n'
                  '|         |   '
                  '+--------------------------------------------------------+            |\n'
                  '|         |   |  PC         (Return Instruction Address to resume)     |  <-- '
                  'SP + 24|\n'
                  '|         |   '
                  '+--------------------------------------------------------+            |\n'
                  '|         |   |  LR (R14)   (Subroutine Link Register)                 |  <-- '
                  'SP + 20|\n'
                  '|         |   '
                  '+--------------------------------------------------------+            |\n'
                  '|         |   |  R12        (Intra-procedure Scratch Register)         |  <-- '
                  'SP + 16|\n'
                  '|         |   '
                  '+--------------------------------------------------------+            |\n'
                  '|         |   |  R3         (Function Parameter / Scratch)             |  <-- '
                  'SP + 12|\n'
                  '|         |   '
                  '+--------------------------------------------------------+            |\n'
                  '|         |   |  R2         (Function Parameter / Scratch)             |  <-- '
                  'SP + 8 |\n'
                  '|         |   '
                  '+--------------------------------------------------------+            |\n'
                  '|         |   |  R1         (Function Parameter / Scratch)             |  <-- '
                  'SP + 4 |\n'
                  '|         |   '
                  '+--------------------------------------------------------+            |\n'
                  '|         v   |  R0         (Function Parameter / Scratch)             |  <-- '
                  'SP (New)|\n'
                  '|             '
                  '+--------------------------------------------------------+            |\n'
                  '|                                                                                   '
                  '|\n'
                  '|    Total Stacking Time: Exactly 12 Clock Cycles (Hardware '
                  'Autonomous)             |\n'
                  '|                                                                                   '
                  '|\n'
                  '+-----------------------------------------------------------------------------------+\n',
 'working_principle': 'Priority Grouping (Preemption vs Sub-Priority):\n'
                      'The NVIC supports up to 256 priority levels (implemented as 16 levels in '
                      'S32K144 using upper 4 bits of priority registers: $0\\text{x}00$ = highest '
                      'priority, $0\\text{xF}0$ = lowest priority). Priority can be split into '
                      '**Preemption Priority** (determines if an interrupt can preempt an actively '
                      'running ISR) and **Sub-Priority** (determines which interrupt executes '
                      'first if two arrive simultaneously).',
 'automotive_application': 'Anti-Lock Braking System (ABS) Wheel Lock Interrupt: An inductive '
                           'wheel speed sensor detects an immediate wheel lockup ($0\\text{ RPM}$) '
                           'during emergency braking. The external pin interrupt asserts IRQ line '
                           'with highest preemption priority ($0\\text{x}00$). The NVIC preempts '
                           'the low-priority dashboard display task within $150\\text{ ns}$ (12 '
                           'cycles at 80 MHz), executing the ABS valve release routine to restore '
                           'tire traction.',
 'comparison_table': {'headers': ['Exception Type',
                                  'Exception Number',
                                  'Priority Level',
                                  'Vector Table Offset',
                                  'Core Purpose'],
                      'rows': [['Initial MSP',
                                '0',
                                'N/A (Hardware reset value)',
                                '0x00000000',
                                'Top of stack memory address'],
                               ['Reset',
                                '1',
                                '-3 (Fixed Highest)',
                                '0x00000004',
                                'First instruction executed on boot'],
                               ['NMI (Non-Maskable)',
                                '2',
                                '-2 (Fixed)',
                                '0x00000008',
                                'Critical hardware failure / Watchdog bite'],
                               ['HardFault',
                                '3',
                                '-1 (Fixed)',
                                '0x0000000C',
                                'Bus error, unaligned access, illegal opcode'],
                               ['SysTick',
                                '15',
                                'Programmable (0 - 15)',
                                '0x0000003C',
                                '1 ms periodic system heartbeat tick for RTOS'],
                               ['Peripheral IRQ (0..n)',
                                '16 to 255',
                                'Programmable (0 - 15)',
                                '0x00000040+',
                                'Hardware peripherals (GPIO, CAN, Timers, ADC)']]},
 'formulas': [{'name': 'Interrupt Latency Calculation',
               'math': 'T_{latency} = \\frac{12 \\text{ clock cycles}}{f_{clock}}',
               'vars': ['12 = Fixed hardware stacking and vector fetch cycles in ARM Cortex-M4',
                        'f_clock = Microcontroller core operating frequency (Hz)'],
               'example': 'On the NXP S32K144 running at f_clock = 80 MHz: T_latency = 12 / (80 × '
                          '10^6) = 150 nanoseconds (0.15 μs).'}],
 'code_snippet': '// CMSIS NVIC Configuration for S32K144 Peripheral Interrupt\n'
                 '#include "S32K144.h"\n'
                 '\n'
                 'void configure_can_interrupt(void) {\n'
                 '    // 1. Set Priority for CAN0 Receive Interrupt (Priority 2, where 0 is '
                 'highest)\n'
                 '    NVIC_SetPriority(CAN0_ORed_0_15_MB_IRQn, 2);\n'
                 '    \n'
                 '    // 2. Clear any pending CAN0 interrupt flag in NVIC\n'
                 '    NVIC_ClearPendingIRQ(CAN0_ORed_0_15_MB_IRQn);\n'
                 '    \n'
                 '    // 3. Enable the Interrupt in NVIC\n'
                 '    NVIC_EnableIRQ(CAN0_ORed_0_15_MB_IRQn);\n'
                 '}\n'
                 '\n'
                 '// Interrupt Service Routine (Vector Table links directly to this function '
                 'name)\n'
                 'void CAN0_ORed_0_15_MB_IRQHandler(void) {\n'
                 '    // Read received CAN message buffer\n'
                 '    process_rx_can_frame();\n'
                 '    // Clear peripheral interrupt flag in FlexCAN controller\n'
                 '    CAN0->IFLAG1 = (1 << 0);\n'
                 '}',
 'must_remember': ['NVIC provides deterministic 12-cycle interrupt entry latency.',
                   'Hardware automatically stacks 8 registers: xPSR, PC, LR, R12, R3, R2, R1, R0.',
                   'Tail-Chaining reduces switchover between consecutive interrupts to only 6 '
                   'clock cycles.',
                   'Lower priority number = HIGHER priority (Priority 0 is higher than Priority '
                   '5).',
                   'Vector Table at 0x00000000 holds Initial MSP (offset 0) and Reset Handler '
                   'address (offset 4).'],
 'short_qa': [('What eight registers are automatically pushed onto the stack by hardware during '
               'ARM Cortex-M4 interrupt entry?',
               'The 8 registers pushed to the stack (the basic stack frame) are: `xPSR`, `PC` '
               '(Program Counter return address), `LR` (Link Register), `R12`, `R3`, `R2`, `R1`, '
               'and `R0`.'),
              ('What is Tail-Chaining in the ARM Cortex-M4 NVIC?',
               'Tail-Chaining is an NVIC hardware optimization where, if another interrupt is '
               'pending when the current ISR completes, the processor skips unstacking and '
               're-stacking the 8 registers, branching directly to the pending ISR in only 6 clock '
               'cycles (saving 18 cycles).')],
 'long_qa': [('Explain the complete ARM Cortex-M4 Exception Model and NVIC operation. Detail the '
              'vector table layout, the 12-cycle hardware stacking sequence, priority grouping '
              '(preemption vs sub-priority), and the Tail-Chaining and Late-Arrival optimizations.',
              'A complete answer covers: (1) Vector table diagram from 0x00000000 (Initial MSP, '
              'Reset, NMI, HardFault, SysTick, IRQs); (2) Step-by-step 12-cycle hardware stacking '
              'diagram showing all 8 registers; (3) EXC_RETURN magic codes; (4) Preemption vs '
              'Sub-priority grouping bits; (5) Tail-Chaining (6-cycle transition) and Late-Arrival '
              'diagrams.')],
 'viva_interview_qa': [('What is the purpose of the special `EXC_RETURN` value loaded into the '
                        'Link Register (LR) when an ISR begins execution?',
                        'In Cortex-M, LR is not loaded with the return address during an '
                        'interrupt. Instead, it is loaded with a special `EXC_RETURN` bit-pattern '
                        '(e.g., $0\\text{xFFFFFFF9}$ or $0\\text{xFFFFFFFD}$). When the ISR '
                        'executes `BX LR` at completion, the hardware detects the `0xFFFFFFF` '
                        'prefix, triggers the automatic hardware unstacking of registers from '
                        'memory, and restores processor mode (Thread/Handler) and active stack '
                        'pointer (MSP/PSP).')],
 'common_mistakes': ['Assuming higher priority numbers mean higher priority. In ARM Cortex-M, '
                     '**lower numerical values represent higher priority** ($0 = \\text{Highest}, '
                     '15 = \\text{Lowest}$).',
                     "Forgetting to clear the peripheral's interrupt flag inside the ISR. If the "
                     'peripheral flag is not cleared, the NVIC will re-trigger the exact same ISR '
                     'indefinitely in an infinite lockup loop.'],
 'revision_points': ['NVIC = 12-cycle deterministic latency.',
                     'Hardware pushes: xPSR, PC, LR, R12, R3, R2, R1, R0.',
                     'Tail-Chaining = 6-cycle transition without restacking.',
                     'Lower priority number = HIGHER priority (0 > 15).',
                     'EXC_RETURN triggers automatic hardware unstacking.'],
 'sources': 'Embedded System Design Lecture 4 & 5 Transcripts; The Definitive Guide to ARM '
            'Cortex-M3/M4 Processors Chapter 7; Course Syllabus Section 4.'},
{'slug': 's32k144-gpio-configuration-and-driver',
 'title': 'NXP S32K144 GPIO Architecture & Low-Level Driver Development',
 'module': 'Microcontroller Peripherals',
 'level': 'Intermediate',
 'importance': 5,
 'overview': 'General Purpose Input/Output (GPIO) ports provide the primary digital interface '
             'between the NXP S32K144 automotive microcontroller and external hardware circuits '
             '(switches, LEDs, relays, and transceivers). S32K144 GPIO configuration requires a '
             '3-tier hardware register hierarchy: Peripheral Clock Control (PCC), Port Control '
             'Register (PORT_PCR for multiplexing, pull-up/down, and pin interrupts), and GPIO '
             'Data Direction / Output Registers (PDDR, PDOR, PSOR, PCOR, PTOR, and PDIR).',
 'learning_objectives': ['Deconstruct the 3-step S32K144 GPIO initialization workflow: Clock '
                         'Gating, Pin Muxing, and Data Direction.',
                         'Configure Peripheral Clock Control (PCC) registers to enable clock trees '
                         'to Port modules.',
                         'Configure Pin Control Registers (PORT_PCRn) for GPIO multiplexing '
                         '(MUX=001), internal pull-up/pull-down, and passive filtering.',
                         'Write bare-metal register-level embedded C drivers to read digital '
                         'inputs and toggle outputs using atomic bit-set and bit-clear registers.'],
 'prerequisites': 'ARM Cortex-M4 Core, Embedded C, Memory-Mapped I/O, Bitwise Operations (`|`, '
                  '`&`, `^`, `~`).',
 'core_concept': 'To maximize energy efficiency, all peripherals in the S32K144 are powered down '
                 'with their clocks turned off upon reset. You cannot simply write to a GPIO pin! '
                 'You must first: (1) Turn ON the clock gate in the PCC module, (2) Configure the '
                 'pin multiplexer in the PORT module so the physical package pin connects to the '
                 'internal GPIO hardware block, and (3) Set pin direction (Input or Output) in the '
                 'GPIO module.',
 'lecture_notes': 'Lecture 2, 4, and 6 of Embedded System Design and Lab Session 1 detailed '
                  'S32K144 GPIO programming. Prof. S. S. Kendre and Prof. Shree Prasad M. '
                  "emphasized: 'The S32K144 has 5 GPIO ports: PTA, PTB, PTC, PTD, and PTE. Each "
                  'pin has a dedicated PORT_PCR register. If you forget to enable the clock in '
                  "PCC_PORTx or forget to set MUX = 0b001, your GPIO code will fail silently!' The "
                  'instructors walked through atomic bit manipulation using PSOR (Set) and PCOR '
                  '(Clear) registers.',
 'extra_explanation': "Let's analyze the **3-Tier S32K144 GPIO Register Hierarchy**:\n"
                      '\n'
                      '1. **Tier 1: Peripheral Clock Control (PCC):**\n'
                      '   - Enables the clock signal to the Port hardware module.\n'
                      '   - Register: `PCC->PCCn[PCC_PORTD_INDEX] |= PCC_PCCn_CGC_MASK;` (Sets '
                      'Clock Gating Control bit).\n'
                      '\n'
                      '2. **Tier 2: Port Control Register (PORT_PCRn):**\n'
                      '   - Configures the electrical characteristics and pin routing of '
                      'individual pin $n$ ($0$ to $31$).\n'
                      '   - **MUX Bits (Bits 10-8):** `000` = Analog, `001` = GPIO, `010-111` = '
                      'Alternate peripheral functions (UART, SPI, CAN, PWM).\n'
                      '   - **PE (Bit 1):** Pull Enable ($1 = \\text{Active}$, $0 = '
                      '\\text{Disabled}$).\n'
                      '   - **PS (Bit 0):** Pull Select ($1 = \\text{Pull-Up}$, $0 = '
                      '\\text{Pull-Down}$).\n'
                      '   - **IRQC (Bits 19-16):** Interrupt Configuration (Rising edge, falling '
                      'edge, both edges, or logic low).\n'
                      '\n'
                      '3. **Tier 3: GPIO Direction & Data Registers (GPIO_Type):**\n'
                      '   - **PDDR (Port Data Direction):** Bit $n = 1$ configures Pin $n$ as '
                      '**Output**; Bit $n = 0$ configures Pin $n$ as **Input**.\n'
                      '   - **PDOR (Port Data Output):** Read/write full 32-bit output latch.\n'
                      '   - **PSOR (Port Set Output):** Writing 1 atomically drives pin HIGH '
                      '(writing 0 has no effect).\n'
                      '   - **PCOR (Port Clear Output):** Writing 1 atomically drives pin LOW '
                      '(writing 0 has no effect).\n'
                      '   - **PTOR (Port Toggle Output):** Writing 1 atomically inverts the pin '
                      'state.\n'
                      '   - **PDIR (Port Data Input):** Read-only register reflecting the physical '
                      'logic level (1 or 0) on the external pin.',
 'workflow_steps': [('Step 1: Enable Clock (PCC)',
                     'PCC->PCCn[PCC_PORTD_INDEX] |= PCC_PCCn_CGC_MASK'),
                    ('Step 2: Pin MUX & Pull (PORT_PCR)',
                     'PORTD->PCR[15] = PORT_PCR_MUX(1) | PORT_PCR_PE_MASK | PORT_PCR_PS_MASK'),
                    ('Step 3: Set Direction (GPIO_PDDR)',
                     'PTD->PDDR |= (1 << 15) for Output; PTD->PDDR &= ~(1 << 15) for Input'),
                    ('Step 4: Output Write / Atomic Control',
                     'PTD->PSOR = (1 << 15) to set High; PTD->PCOR = (1 << 15) to set Low'),
                    ('Step 5: Input Read', 'uint32_t state = (PTD->PDIR >> 15) & 0x01')],
 'diagram_ascii': '\n'
                  '+-----------------------------------------------------------------------------------+\n'
                  '|               NXP S32K144 3-TIER GPIO ARCHITECTURE & DATA '
                  'FLOW                    |\n'
                  '+-----------------------------------------------------------------------------------+\n'
                  '|                                                                                   '
                  '|\n'
                  '|    1. CLOCK GATING '
                  '(PCC)                                                          |\n'
                  '|       [ System Clock 80 MHz ] ---> [ PCC_PORTx (CGC Bit = 1) ] ---> Clock '
                  'Enabled|\n'
                  '|                                                                                   '
                  '|\n'
                  '|    2. PIN MULTIPLEXING '
                  '(PORT_PCRn)                                                |\n'
                  '|       '
                  '+------------------------------------------------------------------------+  |\n'
                  '|       | PORTx_PCRn '
                  'Register                                                    |  |\n'
                  '|       | [ IRQC (19:16) Interrupt ] [ MUX (10:8) = 001 GPIO ] [ PE Pull ] [ PS '
                  ']|  |\n'
                  '|       '
                  '+------------------------------------------------------------------------+  |\n'
                  '|                                         '
                  '|                                         |\n'
                  '|    3. GPIO HARDWARE CORE                '
                  'v                                         |\n'
                  '|       '
                  '+------------------------------------------------------------------------+  |\n'
                  '|       | GPIOx '
                  'Module                                                           |  |\n'
                  '|       '
                  '|                                                                        |  |\n'
                  '|       |  Direction:  PDDR Register (Bit n: 1 = Output, 0 = '
                  'Input)              |  |\n'
                  '|       '
                  '|                                                                        |  |\n'
                  '|       |  Outputs:    PSOR (Atomic Set)   PCOR (Atomic Clear)   PTOR '
                  '(Toggle)   |  |\n'
                  '|       |              -----------------   -------------------   '
                  '-------------   |  |\n'
                  '|       |                      \\                   '
                  '/                             |  |\n'
                  '|       |                       v                 '
                  'v                              |  |\n'
                  '|       |                      [ PDOR Data Output Latch '
                  ']                        |  |\n'
                  '|       |                                 '
                  '|                                      |  |\n'
                  '|       |  Input:              [ PDIR Data Input Buffer ] <==== [ Physical Pin '
                  '] |  |\n'
                  '|       '
                  '+------------------------------------------------------------------------+  |\n'
                  '|                                                                                   '
                  '|\n'
                  '+-----------------------------------------------------------------------------------+\n',
 'working_principle': 'Why Atomic Bit Registers (PSOR / PCOR) are Essential:\n'
                      'In multi-tasking and interrupt-driven embedded systems, modifying a shared '
                      'output register using standard read-modify-write syntax (`PDOR |= (1 << '
                      '15);`) is a major race condition bug: if an interrupt occurs midway through '
                      'the 3-cycle load-or-store instruction sequence, other pin states are '
                      'corrupted. **PSOR and PCOR** allow writing a `1` directly to the target bit '
                      'in a single atomic bus transaction with zero impact on other pins and zero '
                      'race conditions.',
 'automotive_application': 'Brake Pedal Switch Input & Brake Lamp Output: The brake pedal switch '
                           'is connected to Port C Pin 12 with an internal pull-up resistor. When '
                           'the driver presses the brake pedal, PTC12 is pulled to ground (logic '
                           '0). The S32K144 GPIO interrupt reads PDIR, verifies pedal press, and '
                           'immediately drives Port D Pin 15 (Brake Light Relay) HIGH using '
                           '`PTD->PSOR = (1 << 15);` within 10 microseconds.',
 'comparison_table': {'headers': ['Register Name',
                                  'Full Description',
                                  'Access Mode',
                                  'Primary Function'],
                      'rows': [['PCC_PORTx',
                                'Peripheral Clock Control',
                                'Read / Write',
                                'Enables clock gate (CGC bit) to Port module'],
                               ['PORTx_PCRn',
                                'Port Pin Control Register n',
                                'Read / Write',
                                'Pin multiplexer (MUX), pull-up/down, slew rate, interrupt mode'],
                               ['GPIOx_PDDR',
                                'Port Data Direction Register',
                                'Read / Write',
                                'Configures individual pin as Input (0) or Output (1)'],
                               ['GPIOx_PSOR',
                                'Port Set Output Register',
                                'Write Only',
                                'Writing 1 atomically drives pin HIGH (3.3V / 5.0V)'],
                               ['GPIOx_PCOR',
                                'Port Clear Output Register',
                                'Write Only',
                                'Writing 1 atomically drives pin LOW (0.0V Ground)'],
                               ['GPIOx_PTOR',
                                'Port Toggle Output Register',
                                'Write Only',
                                'Writing 1 atomically inverts current output state'],
                               ['GPIOx_PDIR',
                                'Port Data Input Register',
                                'Read Only',
                                'Reads raw digital logic level present on physical external pin']]},
 'formulas': [{'name': 'GPIO Atomic Bit Mask Calculation',
               'math': '\\text{Mask} = (1 \\ll \\text{Pin Number}), \\quad \\text{Set: } '
                       '\\text{PSOR} = \\text{Mask}, \\quad \\text{Clear: } \\text{PCOR} = '
                       '\\text{Mask}',
               'vars': ['Pin Number = Target pin (0 to 31) on Port A, B, C, D, or E',
                        '1 << n = Binary bitmask shifting bit 1 to position n'],
               'example': 'To toggle RGB Blue LED on Port D Pin 0 (PTD0): Mask = (1 << 0) = '
                          '0x00000001. PTD->PTOR = 0x00000001.'}],
 'code_snippet': '// S32K144 Complete Bare-Metal GPIO Driver Example (RGB LED Control)\n'
                 '#include "S32K144.h"\n'
                 '\n'
                 '#define RED_LED_PIN    15  // PTD15\n'
                 '#define BLUE_LED_PIN   0   // PTD0\n'
                 '#define BUTTON_PIN     12  // PTC12 (Input with Pull-Up)\n'
                 '\n'
                 'void gpio_init(void) {\n'
                 '    // 1. Enable Clocks to PORTC and PORTD\n'
                 '    PCC->PCCn[PCC_PORTC_INDEX] |= PCC_PCCn_CGC_MASK;\n'
                 '    PCC->PCCn[PCC_PORTD_INDEX] |= PCC_PCCn_CGC_MASK;\n'
                 '    \n'
                 '    // 2. Configure PTD15 and PTD0 as GPIO Outputs\n'
                 '    PORTD->PCR[RED_LED_PIN] = PORT_PCR_MUX(1);\n'
                 '    PORTD->PCR[BLUE_LED_PIN] = PORT_PCR_MUX(1);\n'
                 '    PTD->PDDR |= (1 << RED_LED_PIN) | (1 << BLUE_LED_PIN);\n'
                 '    \n'
                 '    // 3. Configure PTC12 as GPIO Input with Internal Pull-Up Resistor\n'
                 '    PORTC->PCR[BUTTON_PIN] = PORT_PCR_MUX(1) | PORT_PCR_PE_MASK | '
                 'PORT_PCR_PS_MASK;\n'
                 '    PTC->PDDR &= ~(1 << BUTTON_PIN); // Input direction\n'
                 '}\n'
                 '\n'
                 'int main(void) {\n'
                 '    gpio_init();\n'
                 '    while (1) {\n'
                 '        // Read button state (Active Low: 0 when pressed)\n'
                 '        if ((PTC->PDIR & (1 << BUTTON_PIN)) == 0) {\n'
                 '            PTD->PSOR = (1 << RED_LED_PIN);  // Turn ON Red LED\n'
                 '            PTD->PCOR = (1 << BLUE_LED_PIN); // Turn OFF Blue LED\n'
                 '        } else {\n'
                 '            PTD->PCOR = (1 << RED_LED_PIN);  // Turn OFF Red LED\n'
                 '            PTD->PSOR = (1 << BLUE_LED_PIN); // Turn ON Blue LED\n'
                 '        }\n'
                 '    }\n'
                 '}',
 'must_remember': ['3-step GPIO initialization: (1) Clock in PCC, (2) Pin MUX in PORT_PCR, (3) '
                   'Direction in PDDR.',
                   'MUX = 0b001 (MUX=1) selects GPIO mode in PORT_PCRn.',
                   'Use PSOR (Set) and PCOR (Clear) for atomic thread-safe pin manipulation.',
                   'PDIR is read-only for digital inputs; PDDR configures direction (1=Output, '
                   '0=Input).'],
 'short_qa': [('What are the three essential register configuration steps required to initialize a '
               'GPIO output pin on the NXP S32K144?',
               'Step 1: Enable the peripheral clock for the corresponding Port in the Peripheral '
               'Clock Control (PCC) register (set CGC bit). Step 2: Configure the pin multiplexer '
               'in `PORTx_PCRn` to GPIO mode (`MUX = 001`). Step 3: Set the pin direction bit to '
               'Output (`1`) in the Port Data Direction Register (`GPIOx_PDDR`).'),
              ('Why should an embedded developer use the PSOR and PCOR registers instead of '
               'writing directly to PDOR?',
               'Modifying `PDOR` directly (`PDOR |= (1 << pin)`) requires a multi-cycle '
               'Read-Modify-Write operation that is prone to race conditions if an interrupt '
               'occurs mid-execution. `PSOR` (Set) and `PCOR` (Clear) perform single-cycle atomic '
               'write operations that modify only the targeted pin without affecting other pins on '
               'the port.')],
 'long_qa': [('Explain the complete 3-tier GPIO architecture of the NXP S32K144 microcontroller. '
              'Detail the roles of PCC, PORT, and GPIO register blocks. Write a complete '
              'bare-metal C program to configure Port D Pin 15 as an output LED and Port C Pin 12 '
              'as an input push-button with an internal pull-up resistor.',
              'A complete answer covers: (1) 3-tier register block diagram (PCC -> PORT_PCR -> '
              'GPIO); (2) Explanation of PCC clock gating, PORT_PCR multiplexing/pull-up/interrupt '
              'bits, and GPIO direction/data registers; (3) Explanation of atomic PSOR/PCOR/PTOR '
              'registers; (4) Fully commented bare-metal C code demonstrating clock '
              'initialization, pin muxing, pull-up configuration, and polling loop.')],
 'viva_interview_qa': [('What happens if you attempt to write to `PORTD->PCR[15]` before enabling '
                        '`PCC_PCCn_CGC_MASK` in the PCC register?',
                        'Because the clock tree to PORTD is gated off (unpowered), the bus matrix '
                        'cannot communicate with the PORTD peripheral address space. The CPU core '
                        'encounters a bus access timeout and immediately triggers an unrecoverable '
                        '**BusFault / HardFault** exception.')],
 'common_mistakes': ['Writing to `PORT_PCR` or `GPIO_PDDR` without first enabling the clock in '
                     '`PCC`. This causes an immediate HardFault exception.',
                     'Setting `PTD->PDDR = (1 << 15)` instead of `PTD->PDDR |= (1 << 15)`. Using '
                     '`=` overwrites all other 31 pin directions on that port to inputs!'],
 'revision_points': ['1. PCC: Enable Clock (CGC=1).',
                     '2. PORT_PCR: Set MUX=1 (GPIO) + Pull-up/down.',
                     '3. GPIO_PDDR: 1=Output, 0=Input.',
                     '4. Control: PSOR (Set), PCOR (Clear), PTOR (Toggle), PDIR (Read).'],
 'sources': 'Embedded System Design Lecture 2 & 4 Transcripts; S32K144 Reference Manual Chapter 11 '
            '(PORT) & Chapter 12 (GPIO); Lab 1 Manual.'}
,
{'slug': 's32k144-flexcan-automotive-network-controller',
 'title': 'NXP S32K144 FlexCAN Controller & CAN-FD Implementation',
 'module': 'Microcontroller Peripherals',
 'level': 'Advanced',
 'importance': 5,
 'overview': 'The FlexCAN module in the NXP S32K144 is a full-featured, silicon-hardened '
             'automotive network controller implementing ISO 11898-1 Classic CAN 2.0B and CAN-FD '
             '(Flexible Data-Rate) protocols. Operating with up to 64 flexible Message Buffers '
             '(MBs), individual RX masking, transmit abort capability, and DMA transfers, FlexCAN '
             'enables deterministic inter-ECU communication across vehicle chassis and powertrain '
             'networks.',
 'learning_objectives': ['Analyze the internal architecture of the S32K144 FlexCAN module and its '
                         '64 Message Buffer (MB) RAM array.',
                         'Configure FlexCAN bit-timing registers (PRESDIV, PROPSEG, PSEG1, PSEG2, '
                         'RJW) for 500 kbps Classic CAN and 2 Mbps / 5 Mbps CAN-FD.',
                         'Set up Message Buffer Filter Matching (Individual Mask Registers `RXIMR` '
                         'and Global Mask `RXMGMASK`).',
                         'Implement bare-metal CAN transmission and interrupt-driven reception '
                         'routines.'],
 'prerequisites': 'CAN Protocol Fundamentals, S32K144 Memory Map, Embedded C, NVIC Interrupts.',
 'core_concept': 'The FlexCAN controller offloads 100% of the low-level bit-stuffing, CRC '
                 'calculation, frame acknowledgement, and error frame recovery from the ARM '
                 'Cortex-M4 CPU core. Software interacts with FlexCAN purely through high-level '
                 '**Message Buffers (MBs)** in RAM: you write an ID and payload into a Transmit MB '
                 'and set the code to `TX_ONCE`; the hardware transmits the frame onto the CAN bus '
                 'and generates an interrupt when finished.',
 'lecture_notes': 'Lecture 5 and 6 of Embedded System Design and Lab Session 3 covered FlexCAN on '
                  "the S32K144. Prof. Shree Prasad M. explained: 'FlexCAN has up to 64 Message "
                  'Buffers located in dedicated internal RAM starting at offset $0\\text{x}0080$. '
                  'Each MB contains a Control/Status word, 32-bit ID register, and data payload '
                  "bytes.' The instructor demonstrated configuring FlexCAN in Freeze Mode, setting "
                  'up the 500 kbps bit timing table, and implementing an interrupt handler to read '
                  'incoming brake and speed frames.',
 'extra_explanation': "Let's analyze the **FlexCAN Message Buffer & Register Architecture**:\n"
                      '\n'
                      '1. **Message Buffer (MB) Structure (16 Bytes per MB in Classic CAN):**\n'
                      '   - **Word 0 (Offset $+0\\text{x}0$): Control and Status (CS):**\n'
                      '     - **CODE Field (Bits 27-24):** Indicates MB state:\n'
                      '       - Transmit Codes: `0b1000` (`TX_INACTIVE`), `0b1100` (`TX_ONCE` - '
                      'triggers transmission).\n'
                      '       - Receive Codes: `0b0100` (`RX_EMPTY` - ready to receive), `0b0010` '
                      '(`RX_FULL` - message received).\n'
                      '     - **IDE (Bit 21):** ID Extended ($0 = \\text{Standard 11-bit}$, $1 = '
                      '\\text{Extended 29-bit}$).\n'
                      '     - **RTR (Bit 20):** Remote Transmission Request.\n'
                      '     - **DLC (Bits 19-16):** Data Length Code ($0$ to $8$ bytes).\n'
                      '   - **Word 1 (Offset $+0\\text{x}4$): ID Field:** Standard ID in bits '
                      '28-18 (for 11-bit ID: `ID << 18`).\n'
                      '   - **Words 2 & 3 (Offset $+0\\text{x}8, +0\\text{xC}$):** 8 Data payload '
                      'bytes.\n'
                      '\n'
                      '2. **FlexCAN Initialization Sequence (Freeze Mode):**\n'
                      '   - Step 1: Enable clock in PCC (`PCC->PCCn[PCC_FlexCAN0_INDEX] |= '
                      'PCC_PCCn_CGC_MASK`).\n'
                      '   - Step 2: Request Freeze Mode (`CAN0->MCR |= CAN_MCR_MDIS_MASK;` then '
                      'clear MDIS and assert `FRZ` & `HALT`). Wait for `FRZACK` bit to set.\n'
                      '   - Step 3: Configure Bit Timing in `CAN0->CTRL1` (set nominal bit rate to '
                      '500 kbps).\n'
                      '   - Step 4: Initialize Message Buffers (set MB0 to `RX_EMPTY`, MB1 to '
                      '`TX_INACTIVE`).\n'
                      '   - Step 5: Exit Freeze Mode by clearing `HALT` and `FRZ` bits in `MCR`.',
 'workflow_steps': [('Enter Freeze Mode', 'Assert FRZ & HALT bits in CAN0->MCR; poll FRZACK'),
                    ('Bit Timing Calculation',
                     'Set CAN0->CTRL1 (PRESDIV, PROPSEG, PSEG1, PSEG2) for 500 kbps'),
                    ('Configure RX Message Buffer',
                     'Set MB0 ID=0x120, IDE=0, CODE=0b0100 (RX_EMPTY)'),
                    ('Configure TX Message Buffer',
                     'Set MB1 ID=0x300, IDE=0, CODE=0b1000 (TX_INACTIVE)'),
                    ('Exit Freeze Mode & Transmit',
                     'Clear HALT in MCR; write data payload to MB1; set CODE=0b1100 (TX_ONCE)')],
 'diagram_ascii': '\n'
                  '+-----------------------------------------------------------------------------------+\n'
                  '|               NXP S32K144 FLEXCAN MESSAGE BUFFER RAM '
                  'STRUCTURE                    |\n'
                  '+-----------------------------------------------------------------------------------+\n'
                  '|                                                                                   '
                  '|\n'
                  '|    MESSAGE BUFFER n (Located in FlexCAN Dedicated RAM: 0x40024080 + '
                  'n*0x10)       |\n'
                  '|    '
                  '+--------+----+----+----+----------------------------------------------------+ '
                  '|\n'
                  '|    | Offset | 31 | 30 | 29 | 28  27  26  25  24 | 21  | 20  | 19  18  17  '
                  '16    | |\n'
                  '|    '
                  '+--------+----+----+----+--------------------+-----+-----+-------------------+ '
                  '|\n'
                  '|    | +0x0   | -  | -  | -  |    CODE (4-bit)    | IDE | RTR |    DLC '
                  '(4-bit)    | |\n'
                  '|    '
                  '+--------+----+----+----+--------------------+-----+-----+-------------------+ '
                  '|\n'
                  '|    | +0x4   | PRIO | Standard ID (Bits 28-18)   | Extended ID (Bits '
                  '17-0)       | |\n'
                  '|    '
                  '+--------+------+----------------------------+-------------------------------+ '
                  '|\n'
                  '|    | +0x8   | Data Byte 0 | Data Byte 1         | Data Byte 2 | Data Byte '
                  '3     | |\n'
                  '|    '
                  '+--------+-------------+---------------------+-------------+-----------------+ '
                  '|\n'
                  '|    | +0xC   | Data Byte 4 | Data Byte 5         | Data Byte 6 | Data Byte '
                  '7     | |\n'
                  '|    '
                  '+--------+-------------+---------------------+-------------+-----------------+ '
                  '|\n'
                  '|                                                                                   '
                  '|\n'
                  '|    Code '
                  'States:                                                                   |\n'
                  '|      0b0100 = RX_EMPTY (Ready to receive '
                  'message)                                 |\n'
                  '|      0b0010 = RX_FULL  (New frame in buffer, CPU must '
                  'read)                       |\n'
                  '|      0b1100 = TX_ONCE  (Transmit frame once onto CAN '
                  'bus)                         |\n'
                  '|                                                                                   '
                  '|\n'
                  '+-----------------------------------------------------------------------------------+\n',
 'working_principle': 'Bit Timing Calculation for 500 kbps:\n'
                      'Given a $40\\text{ MHz}$ CAN Protocol Clock ($f_{canclk}$):\n'
                      '- Total Time Quanta per bit ($N_Q$) = $1 + \\text{SyncSeg} + '
                      '\\text{PropSeg} + \\text{PhaseSeg1} + \\text{PhaseSeg2} = 1 + 1 + 6 + 4 + 4 '
                      '= 16\\text{ TQ}$.\n'
                      '- Desired Bit Rate = $500\\text{ kbps} \\implies T_{bit} = 2.0\\ '
                      '\\mu\\text{s}$.\n'
                      '- Time Quantum duration $T_Q = \\frac{T_{bit}}{N_Q} = \\frac{2.0\\ '
                      '\\mu\\text{s}}{16} = 125\\text{ ns}$.\n'
                      '- Prescaler $\\text{PRESDIV} = \\frac{f_{canclk}}{1 / T_Q} = '
                      '\\frac{40\\text{ MHz}}{8\\text{ MHz}} = 5 \\implies '
                      '\\mathbf{\\text{PRESDIV} = 4}$ (0-indexed in register).',
 'automotive_application': 'Automotive Powertrain CAN Gateway Routing: The S32K144 FlexCAN0 '
                           'receives engine RPM and vehicle speed broadcast frames on ID '
                           '$0\\text{x}100$ every 10 ms. The FlexCAN hardware automatically '
                           'filters and stores the frame in MB0, raising an interrupt. The ARM '
                           'core extracts the speed payload and transmits an adjusted target '
                           'suspension damping command onto FlexCAN1 (Chassis CAN) via MB4 in '
                           'under $50\\ \\mu\\text{s}$.',
 'comparison_table': {'headers': ['Feature / Metric',
                                  'Classic CAN 2.0B (FlexCAN)',
                                  'CAN-FD (FlexCAN-FD)',
                                  'LIN 2.2'],
                      'rows': [['Max Data Payload',
                                '8 Bytes per frame',
                                'Up to 64 Bytes per frame',
                                '8 Bytes'],
                               ['Max Baud Rate',
                                '1 Mbps (Typically 500 kbps)',
                                '5 Mbps (Fast data phase) / 8 Mbps',
                                '20 kbps'],
                               ['Hardware Buffers',
                                'Up to 64 Message Buffers',
                                'Up to 32 (64-byte payload MBs)',
                                'Single byte UART buffer'],
                               ['Error Detection',
                                '15-bit CRC + Bit Monitoring + Form Check',
                                '17-bit / 21-bit CRC + Stuff Count',
                                '8-bit Classic Checksum'],
                               ['Automotive Domain',
                                'Powertrain, ABS/ESP, Body Control',
                                'ADAS Radar, EV Inverter Telemetry, Flashing',
                                'Door switches, mirrors, wipers, climate']]},
 'formulas': [{'name': 'CAN Bit Rate and Prescaler Formula',
               'math': '\\text{Bit Rate} = \\frac{f_{canclk}}{(\\text{PRESDIV} + 1) \\times (1 + '
                       '\\text{PROPSEG} + \\text{PSEG1} + \\text{PSEG2} + 3)}',
               'vars': ['f_canclk = Input clock frequency to FlexCAN module (e.g., 40 MHz)',
                        'PRESDIV = Clock prescaler division value (0 to 255)',
                        'PROPSEG, PSEG1, PSEG2 = Segment lengths in time quanta'],
               'example': 'With f_canclk = 40 MHz, PRES_DIV = 4 (div by 5), PROPSEG = 5, PSEG1 = '
                          '3, PSEG2 = 3 (Total 16 TQ): Bit Rate = 40,000,000 / (5 × 16) = '
                          '40,000,000 / 80 = 500,000 bps (500 kbps).'}],
 'code_snippet': '// S32K144 Bare-Metal FlexCAN Transmit Message Routine\n'
                 '#include "S32K144.h"\n'
                 '\n'
                 'void flexcan_transmit_frame(uint32_t standard_id, uint8_t* data, uint8_t dlc) {\n'
                 '    // Use Message Buffer 1 (MB1) for Transmit\n'
                 '    volatile uint32_t* mb1 = (volatile uint32_t*)&(CAN0->RAMn[1 * 4]);\n'
                 '    \n'
                 '    // 1. Set MB1 Code to TX_INACTIVE (0b1000) to prepare buffer\n'
                 '    mb1[0] = (0x8 << 24);\n'
                 '    \n'
                 '    // 2. Set Standard ID (Bits 28-18)\n'
                 '    mb1[1] = (standard_id & 0x7FF) << 18;\n'
                 '    \n'
                 '    // 3. Load Data Payload Bytes\n'
                 '    mb1[2] = ((uint32_t)data[0] << 24) | ((uint32_t)data[1] << 16) | \n'
                 '             ((uint32_t)data[2] << 8)  | ((uint32_t)data[3]);\n'
                 '    mb1[3] = ((uint32_t)data[4] << 24) | ((uint32_t)data[5] << 16) | \n'
                 '             ((uint32_t)data[6] << 8)  | ((uint32_t)data[7]);\n'
                 '             \n'
                 '    // 4. Start Transmission: Set CODE = 0b1100 (TX_ONCE), IDE=0, DLC\n'
                 '    mb1[0] = (0xC << 24) | ((dlc & 0x0F) << 16);\n'
                 '}',
 'must_remember': ['FlexCAN supports up to 64 hardware Message Buffers in dedicated RAM '
                   '(0x40024080).',
                   'To configure bit rates, FlexCAN MUST be placed into Freeze Mode (FRZ & HALT).',
                   'Standard 11-bit CAN ID is placed in bits 28-18 of Word 1 (`ID << 18`).',
                   'TX_ONCE code (`0b1100`) triggers automatic autonomous hardware frame '
                   'transmission.',
                   'CAN-FD supports up to 64-byte payloads at data bitrates up to 5-8 Mbps.'],
 'short_qa': [('What are the two steps required to put the S32K144 FlexCAN controller into Freeze '
               'Mode for configuration?',
               'Step 1: Set the `FRZ` (Freeze Enable) and `HALT` bits in the Module Configuration '
               'Register (`CAN0->MCR`). Step 2: Poll the `FRZACK` (Freeze Acknowledge) bit in '
               '`CAN0->MCR` until hardware asserts it high, confirming that the CAN state machine '
               'is frozen.'),
              ('What is the difference between Message Buffer Code `0b0100` and `0b0010` during '
               'FlexCAN reception?',
               'Code `0b0100` (`RX_EMPTY`) configures the Message Buffer as active and waiting to '
               'receive an incoming CAN frame. Code `0b0010` (`RX_FULL`) is set automatically by '
               'hardware when a matching CAN frame has been received and written into the buffer, '
               'signaling the CPU to read the payload.')],
 'long_qa': [('Explain the architecture and memory layout of Message Buffers in the NXP S32K144 '
              'FlexCAN module. Detail the bitfields of Word 0 (Control/Status) and Word 1 (ID). '
              'Calculate the register timing parameters to achieve a 500 kbps bit rate from a 40 '
              'MHz CAN clock.',
              'A complete answer covers: (1) FlexCAN RAM memory map diagram from offset 0x0080; '
              '(2) Detailed bitfield diagram of Word 0 (CODE, IDE, RTR, DLC, TIMESTAMP) and Word 1 '
              '(Standard/Extended ID); (3) Explanation of RX_EMPTY, RX_FULL, TX_INACTIVE, and '
              'TX_ONCE codes; (4) Step-by-step bit timing derivation showing TQ=16, PRES_DIV=4, '
              'PROPSEG=5, PSEG1=3, PSEG2=3 to achieve exactly 500 kbps from 40 MHz clock.')],
 'viva_interview_qa': [('Why does the CPU have to read the Timer Free-Running Register '
                        '(`CAN0->TIMER`) after reading a received Message Buffer payload in an '
                        'ISR?',
                        'Reading the `CAN0->TIMER` register unlocks the Message Buffer RAM array '
                        'in hardware. If the software reads the MB payload but forgets to read '
                        '`CAN0->TIMER`, the FlexCAN controller keeps the internal buffer locked, '
                        'preventing new incoming CAN frames from being received in that buffer.')],
 'common_mistakes': ['Writing the 11-bit CAN Standard ID starting at bit 0 instead of bit 18. In '
                     'FlexCAN, Standard IDs MUST be shifted left by 18 bits (`ID << 18`).',
                     'Attempting to write to `CAN0->CTRL1` while the controller is running outside '
                     'Freeze Mode. Timing registers are write-protected outside Freeze Mode.'],
 'revision_points': ['64 MBs in RAM at 0x40024080.',
                     'Freeze Mode (FRZ + HALT) required to change bit timing.',
                     'Standard ID shifted by 18 bits: ID << 18.',
                     'TX_ONCE = 0b1100 triggers transmission.',
                     'Read CAN0->TIMER to unlock MB after RX.'],
 'sources': 'Embedded System Design Lecture 5 & 6 Transcripts; S32K144 Reference Manual Chapter 53 '
            '(FlexCAN); ESD Lab 3 Manual.'}
]
