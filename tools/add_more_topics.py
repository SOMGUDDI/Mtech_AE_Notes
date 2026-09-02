"""Adds further deep topics for Automotive Vehicle, Autotronics, and Embedded System Design."""
import sys
from pathlib import Path
import pprint

TOOLS_DIR = Path(__file__).resolve().parent

AV_TOPICS_2 = [
    {
        "slug": "ev-motors-inverters-battery-packs",
        "title": "EV Powertrains: Traction Motors, Inverters & Battery Packs",
        "module": "Electric & Hybrid Vehicles",
        "level": "Advanced",
        "importance": 5,
        "overview": "Electric vehicle powertrains replace internal combustion engines and multi-speed gearboxes with three core high-voltage mechatronic subsystems: the High-Voltage Traction Battery Pack (Li-Ion NMC/LFP), the 3-Phase Traction Inverter (IGBT / Silicon Carbide SiC MOSFETs), and the Traction Electric Motor (Permanent Magnet Synchronous Motor PMSM or AC Induction Motor ACIM).",
        "learning_objectives": [
            "Compare EV motor topologies: Permanent Magnet Synchronous Motors (PMSM) vs AC Induction Motors (ACIM).",
            "Explain 3-Phase Inverter architecture and Space Vector Pulse Width Modulation (SVPWM).",
            "Analyze Lithium-Ion battery cell chemistry (NMC vs LFP), C-Rate, State of Charge (SOC), and State of Health (SOH).",
            "Understand High-Voltage Battery Management Systems (BMS): Cell balancing, thermal runaway prevention, and pre-charge contactor sequencing."
        ],
        "prerequisites": "Automotive Systems Signal Flow, Transistors & Power Electronics, Tractive Force.",
        "core_concept": "In an EV, DC chemical energy stored in thousands of battery cells (~400V or 800V) flows through heavy copper busbars to the Inverter. The inverter acts as an ultra-high-speed electronic commutator, switching 6 silicon carbide MOSFETs thousands of times per second to synthesize smooth 3-phase sinusoidal AC currents that generate a rotating magnetic field in the motor stator, pulling the rotor with immense electromagnetic torque.",
        "lecture_notes": "Lecture 2 and 3 covered EV powertrains. The professor emphasized: 'EVs decouple mechanical speed from torque using variable-frequency inverter control. Unlike an engine that must reach 4000 RPM to develop peak torque, a PMSM electric motor produces maximum torque from 0 RPM.' The lecturer analyzed 400V vs 800V architectures, explaining how doubling bus voltage halves current ($I = P/V$), which reduces cable $I^2 R$ heat losses by 75% and enables 350 kW ultra-fast DC charging.",
        "extra_explanation": "Let's analyze the three core EV subsystems:\n\n1. **Traction Electric Motors:**\n   - **PMSM (Permanent Magnet Synchronous Motor):** Rotor contains NdFeB permanent magnets. Offers highest power density ($> 4\\text{ kW/kg}$) and peak efficiency ($> 97\\%$). Dominant in modern passenger EVs.\n   - **ACIM (AC Induction Motor):** Rotor uses copper/aluminum squirrel cage bars; rotor field is induced magnetically. Zero rare-earth magnets, low cost, excellent high-speed freewheeling efficiency.\n\n2. **3-Phase Inverter & Power Electronics:**\n   - Consists of 6 power switches in a 3-leg bridge configuration.\n   - Modern 800V EVs use **Silicon Carbide (SiC) Wide-Bandgap MOSFETs**, which switch at 20–50 kHz with 70% lower switching losses than traditional silicon IGBTs.\n\n3. **Traction Battery Pack & Battery Management System (BMS):**\n   - **NMC (Nickel Manganese Cobalt):** High energy density ($250\\text{ Wh/kg}$), excellent range, higher thermal runaway risk ($> 210^\\circ\\text{C}$).\n   - **LFP (Lithium Iron Phosphate):** Lower energy density ($160\\text{ Wh/kg}$), ultra-safe ($270^\\circ\\text{C}$ thermal stability), 3000+ deep charge cycles, lower cost.\n   - **C-Rate:** Measure of charge/discharge speed. $1\\text{C}$ discharges a $75\\text{ kWh}$ battery in 1 hour ($75\\text{ kW}$); $4\\text{C}$ DC fast charging charges it in 15 minutes ($300\\text{ kW}$).",
        "workflow_steps": [
            ("Driver Throttle Input", "Pedal sensor sends torque demand signal to Powertrain Controller"),
            ("BMS Contactor Pre-charge", "Pre-charge resistor limits inrush current; main DC contactors close"),
            ("Inverter SVPWM Synthesis", "Space Vector PWM modulates 6 SiC MOSFETs to create rotating stator flux"),
            ("Electromagnetic Torque Generation", "Stator field pulls rotor magnets, generating smooth drive torque"),
            ("Regenerative Braking Energy Harvest", "Motor acts as generator during deceleration; inverter rectifies AC to DC to recharge battery")
        ],
        "diagram_ascii": """
+-----------------------------------------------------------------------------------+
|               ELECTRIC VEHICLE HIGH-VOLTAGE POWERTRAIN TOPOLOGY                   |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|    +------------------------+             +----------------------------------+    |
|    | HIGH-VOLTAGE BATTERY   |  400V /     | 3-PHASE TRACTION INVERTER        |    |
|    | PACK (400V / 800V DC)  |  800V DC    | (6x Silicon Carbide SiC MOSFETs) |    |
|    |                        |             |                                  |    |
|    | [ CELL ] [ CELL ] ...  |====[+]=====>|    +--[S1]--+  +--[S3]--+  +--[S5]--+|    |
|    | [ CELL ] [ CELL ] ...  |  (Busbar)   |    |        |  |        |  |        ||    |
|    |                        |             |    +---U----+  +---V----+  +---W----+|    |
|    | [ BMS CONTROLLER ]     |             |    |        |  |        |  |        ||    |
|    | (Balancing & Thermal)  |====[-]=====>|    +--[S2]--+  +--[S4]--+  +--[S6]--+|    |
|    +------------------------+             +----+--------+-----------+-------+----+    |
|                                                |            |           |         |
|                                                v (Phase U)  v (Phase V) v (Phase W)
|                                            +------------------------------------+ |
|                                            | 3-PHASE PMSM TRACTION MOTOR        | |
|                                            | (Stator Windings + NdFeB Rotor)    | |
|                                            |                                    | |
|                                            |             ( Rotor )              | |
|                                            +-----------------+------------------+ |
|                                                              | (Shaft Torque)     |
|                                                              v                    |
|                                            [ Single-Speed Reduction Gear (9:1) ]  |
|                                                              |                    |
|                                                              v                    |
|                                                (O) Driven Wheels (O)              |
|                                                                                   |
+-----------------------------------------------------------------------------------+
""",
        "working_principle": "High-Voltage Pre-Charge Contactor Sequence:\nThe inverter contains massive DC bus smoothing capacitors ($C_{bus} \\approx 1000\\ \\mu\\text{F}$). If the main $400\\text{V}$ battery contactor closed directly, the uncharged capacitor would act as a dead short circuit, pulling an inrush current of $I = \\frac{400\\text{V}}{0.05\\ \\Omega} = \\mathbf{8000\\text{ Amperes}}$, welding the contactor shut and blowing fuses. The BMS sequences a **Pre-charge Relay** with a $50\\ \\Omega$ resistor in series for $200\\text{ ms}$ to gently charge the DC bus to 95% voltage before closing the main high-current contactor.",
        "automotive_application": "Regenerative Braking Blending in EVs: When the driver taps the brake pedal, the vehicle brake control unit commands the inverter to operate in reverse (regenerative mode). The electric motor generates up to 70 kW of electric power, converting the vehicle's kinetic energy back into chemical energy in the battery, bringing the vehicle to a halt while recovering up to 25% of urban driving energy and extending brake pad life past 150,000 km.",
        "comparison_table": {
            "headers": ["Subsystem / Parameter", "PMSM Traction Motor", "AC Induction Motor (ACIM)", "IC Engine Powertrain"],
            "rows": [
                ["Peak Efficiency", "96% to 97.5% (Extremely high)", "93% to 95%", "32% to 40% (Thermodynamically limited)"],
                ["Power Density", "4.0 to 6.0 kW/kg (Compact)", "2.5 to 3.5 kW/kg", "0.8 to 1.5 kW/kg"],
                ["Rotor Construction", "Neodymium Permanent Magnets (NdFeB)", "Copper/Aluminum Squirrel Cage", "Pistons, Crankshaft, Connecting rods"],
                ["Max Operating Speed", "16,000 to 20,000 RPM", "14,000 to 18,000 RPM", "6,000 to 7,000 RPM"],
                ["Zero-RPM Torque", "100% Maximum Instant Torque", "100% Maximum Instant Torque", "0 Nm (Stalls without clutch slip)"]
            ]
        },
        "formulas": [
            {
                "name": "Battery Pack Capacity and Range Energy Calculation",
                "math": "E_{pack} = N_s \\times N_p \\times V_{cell,nom} \\times C_{cell} \\quad [\\text{Wh}]",
                "vars": [
                    "N_s = Number of cells connected in series (determines total pack voltage)",
                    "N_p = Number of cells connected in parallel (determines total pack Ah capacity)",
                    "V_cell,nom = Nominal cell voltage (3.7V for NMC, 3.2V for LFP)",
                    "C_cell = Capacity of individual cell (Ampere-hours, Ah)"
                ],
                "example": "A pack has 96S 4P configuration with 3.7V 50Ah NMC cells. Pack Voltage = 96 × 3.7V = 355.2 V. Pack Ah = 4 × 50Ah = 200 Ah. Total Energy = 355.2V × 200Ah = 71,040 Wh = 71.04 kWh."
            }
        ],
        "code_snippet": """// Python EV Battery Pack Sizing and Inrush Current Calculator
def size_ev_battery(target_kwh=75.0, cell_voltage=3.7, cell_ah=50.0, nominal_pack_v=400.0):
    n_series = int(nominal_pack_v / cell_voltage)
    actual_pack_v = n_series * cell_voltage
    
    total_ah_needed = (target_kwh * 1000.0) / actual_pack_v
    n_parallel = int(round(total_ah_needed / cell_ah))
    
    actual_kwh = (n_series * actual_pack_v * cell_ah * n_parallel) / (n_series * 1000.0)
    
    print(f"EV Battery Architecture: {n_series}S {n_parallel}P")
    print(f"  Nominal Voltage : {actual_pack_v:.1f} V")
    print(f"  Total Capacity  : {n_parallel * cell_ah:.1f} Ah")
    print(f"  Energy Stored   : {actual_kwh:.2f} kWh")
    print(f"  Total Cells     : {n_series * n_parallel} individual cells")

size_ev_battery(target_kwh=75.0)""",
        "must_remember": [
            "EV powertrain = Battery Pack (DC) + 3-Phase Inverter + AC Electric Traction Motor.",
            "PMSM offers highest efficiency (>97%) and power density using NdFeB rotor magnets.",
            "800V architectures halve current (I = P/V), reducing I^2 R heat losses by 75% for 350kW charging.",
            "BMS pre-charge sequencing prevents 8000A inrush current from destroying inverter capacitors."
        ],
        "short_qa": [
            ("Why are 800V battery architectures rapidly replacing 400V systems in modern premium EVs?", "Operating at 800V delivers the same electric power ($P = V \\cdot I$) with half the current ($I$). Halving current reduces Joule heating losses ($I^2 R$) in wiring harnesses and battery cells by **75%**, allows thinner and lighter copper cables, and enables 350 kW DC ultra-fast charging (10% to 80% in 18 minutes)."),
            ("What is the difference between active and passive cell balancing in a Battery Management System (BMS)?", "Passive balancing bleeds off excess energy from higher-voltage cells as waste heat through parallel bypass resistors. Active balancing uses bidirectional DC-DC inductive/capacitive converters to shuttle energy from higher-voltage cells into weaker cells without wasting energy as heat.")
        ],
        "long_qa": [
            ("Explain the architecture, power flow, and component interactions of an Electric Vehicle powertrain from high-voltage battery to driven wheels. Include the 3-phase inverter bridge, PMSM motor operation, and the BMS pre-charge sequencing procedure.", "A complete answer covers: (1) System topology diagram connecting battery, BMS, DC bus, 3-phase inverter, motor, and reduction gear; (2) Detailed operation of PMSM and Space Vector PWM; (3) NMC vs LFP cell chemistries; (4) Pre-charge contactor timing sequence and inrush current calculation; (5) Regenerative braking energy recovery mechanism.")
        ],
        "viva_interview_qa": [
            ("What is 'Thermal Runaway' in a Lithium-Ion battery and how does a modern automotive BMS mitigate it?", "Thermal runaway is an uncontrollable exothermic self-heating chain reaction that occurs when internal cell temperature exceeds ~150°C (due to internal short, overcharging, or physical puncture). The separator melts, releasing oxygen from the cathode, causing rapid fire and venting. The BMS mitigates this via continuous millivolt cell monitoring, liquid glycol cooling plates, pyrotechnic battery disconnect fuses, and aerogel thermal barrier blankets between cells.")
        ],
        "common_mistakes": [
            "Assuming an EV motor uses DC electricity directly from the battery. Traction motors are almost universally **3-Phase AC motors** driven by an electronic inverter.",
            "Confusing Battery Power (kW) with Battery Energy Capacity (kWh). kW is instantaneous power (acceleration rate); kWh is energy volume (total driving range)."
        ],
        "revision_points": [
            "Battery (DC) -> Inverter (SVPWM) -> Motor (3-Phase AC).",
            "PMSM = Permanent Magnets, 97% peak efficiency.",
            "800V = 50% current, 75% less I^2 R heat.",
            "Pre-charge resistor prevents capacitor inrush damage."
        ],
        "sources": "Automotive Vehicle Lecture 2 & 3 Transcripts; Session 2 EV Fundamentals PDF; Syllabus Section 3 & 4."
    }
]

AT_TOPICS_2 = [
    {
        "slug": "analog-to-digital-and-digital-to-analog-converters",
        "title": "Data Converters: ADC & DAC Architectures in Automotive ECUs",
        "module": "Analog-to-Digital Conversion",
        "level": "Intermediate",
        "importance": 5,
        "overview": "Microcontrollers operate strictly in the discrete digital domain (1s and 0s), whereas automotive physical phenomena (temperatures, manifold pressures, throttle angles, and oxygen levels) exist as continuous analog voltages. Analog-to-Digital Converters (ADCs) digitize these continuous voltages, while Digital-to-Analog Converters (DACs) synthesize continuous analog voltages for actuator commands.",
        "learning_objectives": [
            "Define ADC performance metrics: Resolution ($n$-bits), Reference Voltage ($V_{ref}$), Quantization Step Size (LSB), and Quantization Error ($\\pm 0.5\\text{ LSB}$).",
            "Analyze Successive Approximation Register (SAR) ADC binary search architecture.",
            "Understand Flash ADC, Sigma-Delta ($\\Sigma-\\Delta$) ADC, and R-2R Ladder DAC architectures.",
            "Apply the Nyquist-Shannon Sampling Theorem ($f_s \\ge 2 f_{max}$) and design anti-aliasing filters."
        ],
        "prerequisites": "Op-Amps in Signal Conditioning, Voltage Dividers, Digital Logic Gates.",
        "core_concept": "An ADC chops continuous real-world voltage into discrete numerical stairs. A 10-bit ADC dividing a 5.0V supply into $2^{10} = 1024$ voltage levels has a step size (LSB) of $4.88\\text{ mV}$. If the input voltage is $2.500\\text{ V}$, the ADC outputs binary code `1000000000` ($512$).",
        "lecture_notes": "Lecture 5 and 6 of Autotronics covered ADC and DAC converters. Dr. Madhuri Bayya emphasized: 'The ADC resolution determines the smallest physical change you can detect. For a 12-bit ADC with 5V reference, 1 LSB is $5 / 4096 = 1.22\\text{ mV}$. If your knock sensor signal is smaller than 1.22 mV, the ADC is completely blind to it!' The instructor walked through the SAR binary search flowchart and the Nyquist sampling criterion.",
        "extra_explanation": "Let's analyze the governing mathematical principles:\n\n1. **ADC Resolution and Least Significant Bit (LSB):**\n   $$\\text{LSB Step Size } (q) = \\frac{V_{ref+} - V_{ref-}}{2^n} = \\frac{V_{ref}}{2^n}$$\n   - Digital Output Code: $\\text{Code} = \\text{floor}\\left( \\frac{V_{in}}{V_{ref}} \\times 2^n \\right)$\n   - Quantization Error: Unavoidable rounding error bounded by $\\pm \\frac{1}{2} \\text{ LSB} = \\pm \\frac{q}{2}$.\n\n2. **Successive Approximation Register (SAR) ADC Operation:**\n   - Uses a binary search algorithm to resolve $n$ bits in exactly $n$ clock cycles.\n   - **Step 1:** Sample-and-Hold circuit freezes input voltage $V_{in}$.\n   - **Step 2:** SAR sets Most Significant Bit (MSB, Bit $n-1$) to 1. Internal DAC outputs $V_{DAC} = 0.5 V_{ref}$.\n   - **Step 3:** Analog comparator compares $V_{in}$ with $V_{DAC}$. If $V_{in} > V_{DAC}$, MSB remains 1; if $V_{in} < V_{DAC}$, MSB is cleared to 0.\n   - **Step 4:** SAR moves to next bit ($n-2$) and repeats until all $n$ bits are evaluated.\n\n3. **Nyquist-Shannon Sampling Theorem:**\n   $$f_s \\ge 2 \\cdot f_{max}$$\n   - The sampling frequency ($f_s$) must be at least twice the highest frequency component ($f_{max}$) present in the analog signal. If $f_s < 2 f_{max}$, high frequencies fold back into the lower spectrum (**Aliasing distortion**). An analog low-pass **Anti-Aliasing Filter** must precede every ADC.",
        "workflow_steps": [
            ("Analog Signal Conditioning", "Op-amp buffers and filters sensor signal to 0-5V band"),
            ("Anti-Aliasing Low-Pass Filter", "Attenuates frequencies above Nyquist limit (f_s / 2)"),
            ("Sample and Hold (S/H)", "S/H switch closes for t_sample, charging internal sampling capacitor"),
            ("SAR Binary Search Conversion", "SAR evaluates bits MSB to LSB over 12 clock cycles"),
            ("Interrupt & Digital Register Read", "Conversion Complete flag sets; MCU reads 12-bit binary result")
        ],
        "diagram_ascii": """
+-----------------------------------------------------------------------------------+
|               SUCCESSIVE APPROXIMATION REGISTER (SAR) ADC ARCHITECTURE            |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|    Analog Input (Vin)                                                             |
|           o--------[ S/H Switch ]---+                                             |
|                                     |                                             |
|                                  [ C_hold ]                                       |
|                                     |                                             |
|                                     v (+)                                         |
|                                  |\                                               |
|                                  | \                                              |
|                                  |  \ Comparator Output                           |
|                                  |   \----------------+                           |
|                                  |  /                 |                           |
|                                  | /                  v                           |
|                             +----|-/       +-----------------------+              |
|                             |    |/        |  SUCCESSIVE           |              |
|                             |  (-)         |  APPROXIMATION        |===> 12-Bit   |
|                             |              |  REGISTER (SAR) LOGIC |     Digital  |
|                             |              +-----------+-----------+     Output   |
|                             |                          |                          |
|                             |              +-----------v-----------+              |
|                             +--------------| INTERNAL R-2R DAC     |              |
|                                            | (Generates V_test)    |              |
|                                            +-----------------------+              |
|                                                                                   |
|    SAR Binary Search: Resolves 12 bits in exactly 12 clock cycles!                |
|                                                                                   |
+-----------------------------------------------------------------------------------+
""",
        "working_principle": "Worked ADC Quantization Calculation:\nConsider a 12-bit ADC in the NXP S32K144 MCU with $V_{ref} = 5.00\\text{ V}$:\n- Number of discrete quantization levels = $2^{12} = 4096$.\n- LSB Step Size $q = \\frac{5.00\\text{ V}}{4096} = \\mathbf{1.2207\\text{ mV}}$.\n- If a Manifold Absolute Pressure (MAP) sensor inputs $V_{in} = 3.456\\text{ V}$:\n  $$\\text{Digital Code} = \\text{round}\\left( \\frac{3.456}{5.00} \\times 4096 \\right) = \\text{round}(2831.15) = \\mathbf{2831} \\quad (0\\text{xB0F})$$\n- Voltage reconstructed by ECU: $V_{calc} = 2831 \\times 1.2207\\text{ mV} = 3.4558\\text{ V}$ (Quantization error = $-0.2\\text{ mV}$).",
        "automotive_application": "Crankshaft Position Variable Reluctance (VR) Sensor Digitization: A 60-2 tooth reluctor wheel spinning at 6000 RPM produces an analog AC sine wave with frequency $f = 6000/60 \\times 60 = 6000\\text{ Hz}$ ($6\\text{ kHz}$). According to Nyquist, the ADC must sample at $f_s > 12\\text{ kHz}$. The engine ECU samples at $50\\text{ kHz}$ to capture crisp zero-crossing points for microsecond-accurate fuel injection timing.",
        "comparison_table": {
            "headers": ["ADC Architecture", "Conversion Speed", "Resolution", "Silicon Complexity & Cost", "Primary Automotive Application"],
            "rows": [
                ["Successive Approximation (SAR)", "Medium (1 to 5 MSPS; 1 cycle/bit)", "10 to 16 bits", "Low to Moderate", "General MCU on-chip ADCs (S32K144, sensors, pedals)"],
                ["Flash (Parallel Comparator)", "Ultra-Fast (100 to 1000 MSPS; 1 cycle)", "6 to 8 bits", "Very High (Requires 2^n - 1 comparators)", "Radar/LIDAR front-end, high-speed oscilloscope"],
                ["Sigma-Delta (Σ-Δ)", "Slow to Medium (Oversampled)", "16 to 24 bits (Ultra-high)", "Moderate (Digital filter heavy)", "Precision EV battery cell monitoring, strain gauges"],
                ["Dual-Slope Integrating", "Very Slow (Hundreds of ms)", "14 to 18 bits", "Low (Immune to 50Hz noise)", "Handheld automotive digital multimeters (DMM)"]
            ]
        },
        "formulas": [
            {
                "name": "ADC Output Code and Voltage Relationship",
                "math": "\\text{Code} = \\frac{V_{in}}{V_{ref}} \\times (2^n - 1), \\quad V_{in} = \\frac{\\text{Code}}{2^n - 1} \\times V_{ref}",
                "vars": [
                    "V_in = Analog input voltage (0 to V_ref)",
                    "V_ref = ADC reference supply voltage (e.g., 5.0V or 3.3V)",
                    "n = Bit resolution of the ADC (e.g., 10, 12, or 16 bits)",
                    "Code = Integer output value (0 to 2^n - 1)"
                ],
                "example": "A 10-bit ADC (2^10 - 1 = 1023) with Vref = 5.0V reads Code = 768. The measured voltage is Vin = (768 / 1023) × 5.0V = 3.7537 Volts."
            },
            {
                "name": "Signal-to-Quantization-Noise Ratio (SQNR)",
                "math": "\\text{SQNR} = 6.02 \\cdot n + 1.76 \\quad [\\text{dB}]",
                "vars": [
                    "n = Number of ADC bits",
                    "SQNR = Theoretical maximum dynamic range (dB)"
                ],
                "example": "For a 12-bit ADC: SQNR = (6.02 × 12) + 1.76 = 72.24 + 1.76 = 74.0 dB."
            }
        ],
        "code_snippet": """// C Code to Convert S32K144 12-bit ADC Code to Scaled Sensor Physical Units
#include <stdint.h>

float adc_to_temperature_celsius(uint16_t adc_code, float v_ref) {
    // 1. Convert 12-bit ADC raw code (0-4095) to analog voltage
    float voltage = ((float)adc_code / 4095.0f) * v_ref;
    
    // 2. Linear temperature calibration (e.g., 10 mV / °C with 500 mV offset at 0°C)
    // Sensor equation: V_out = 0.500V + (0.010V/°C * Temp)
    float temperature_c = (voltage - 0.500f) / 0.010f;
    return temperature_c;
}""",
        "must_remember": [
            "ADC LSB step size: q = V_ref / 2^n (1.22 mV for 12-bit 5V ADC).",
            "SAR ADC resolves n bits in n clock cycles using binary search.",
            "Nyquist theorem: Sampling frequency fs >= 2 * f_max to avoid aliasing.",
            "Anti-aliasing low-pass filter MUST precede the ADC input.",
            "Flash ADC is fastest (1 cycle) but requires 2^n - 1 comparators."
        ],
        "short_qa": [
            ("What is the LSB step size and quantization error of a 10-bit ADC operating from a 5.0V reference?", "The LSB step size is $q = \\frac{5.0\\text{ V}}{2^{10}} = \\frac{5.0}{1024} = \\mathbf{4.88\\text{ mV}}$. The maximum quantization error is $\\pm 0.5\\text{ LSB} = \\mathbf{\\pm 2.44\\text{ mV}}$."),
            ("State the Nyquist-Shannon Sampling Theorem and explain the consequence of violating it.", "The Nyquist-Shannon theorem states that an analog signal must be sampled at a rate $f_s \\ge 2 f_{max}$, where $f_{max}$ is the highest frequency present in the signal. Violating this theorem causes high-frequency components to fold back into the lower frequency spectrum as false, distorted frequencies (**Aliasing**).")
        ],
        "long_qa": [
            ("Explain the architecture and complete step-by-step conversion cycle of a Successive Approximation Register (SAR) ADC. For a 4-bit SAR ADC with $V_{ref} = 5.0\\text{ V}$ and analog input $V_{in} = 3.2\\text{ V}$, trace the comparator decisions and register contents across all 4 clock cycles.", "A complete answer covers: (1) Block diagram of SAR ADC (S/H, Comparator, SAR logic, DAC); (2) Step size q = 5.0 / 16 = 0.3125V; (3) Cycle-by-cycle trace: Cycle 1 (Test 1000 = 2.5V: Vin > 2.5V -> Bit3=1), Cycle 2 (Test 1100 = 3.75V: Vin < 3.75V -> Bit2=0), Cycle 3 (Test 1010 = 3.125V: Vin > 3.125V -> Bit1=1), Cycle 4 (Test 1011 = 3.4375V: Vin < 3.4375V -> Bit0=0); (4) Final output binary code = 1010 (Decimal 10, reconstructed voltage 3.125V).")
        ],
        "viva_interview_qa": [
            ("Why does a Flash ADC become impractical for high resolutions like 16 bits?", "A Flash ADC requires $2^n - 1$ physical analog comparators operating in parallel. For an 8-bit Flash ADC, it needs $255$ comparators (feasible). For a 16-bit Flash ADC, it would require $2^{16} - 1 = \\mathbf{65,535\\text{ analog comparators}}$ on a single die, drawing tens of amperes of current and consuming massive silicon area.")
        ],
        "common_mistakes": [
            "Dividing by $2^n - 1$ instead of $2^n$ when calculating LSB step size.",
            "Omission of an anti-aliasing low-pass filter ahead of the ADC. Software filtering CANNOT remove aliasing once the signal is digitized."
        ],
        "revision_points": [
            "LSB = V_ref / 2^n.",
            "SAR = Binary search, n clock cycles.",
            "Nyquist: f_s >= 2 * f_max.",
            "Flash ADC = 2^n - 1 comparators (Fastest).",
            "SQNR = 6.02 * n + 1.76 dB."
        ],
        "sources": "Autotronics Lecture 5 & 6 Transcripts; Course Syllabus Section 6 (Data Acquisition and Conversion)."
    }
]

ESD_TOPICS_2 = [
    {
        "slug": "s32k144-flexcan-automotive-network-controller",
        "title": "NXP S32K144 FlexCAN Controller & CAN-FD Implementation",
        "module": "Microcontroller Peripherals",
        "level": "Advanced",
        "importance": 5,
        "overview": "The FlexCAN module in the NXP S32K144 is a full-featured, silicon-hardened automotive network controller implementing ISO 11898-1 Classic CAN 2.0B and CAN-FD (Flexible Data-Rate) protocols. Operating with up to 64 flexible Message Buffers (MBs), individual RX masking, transmit abort capability, and DMA transfers, FlexCAN enables deterministic inter-ECU communication across vehicle chassis and powertrain networks.",
        "learning_objectives": [
            "Analyze the internal architecture of the S32K144 FlexCAN module and its 64 Message Buffer (MB) RAM array.",
            "Configure FlexCAN bit-timing registers (PRESDIV, PROPSEG, PSEG1, PSEG2, RJW) for 500 kbps Classic CAN and 2 Mbps / 5 Mbps CAN-FD.",
            "Set up Message Buffer Filter Matching (Individual Mask Registers `RXIMR` and Global Mask `RXMGMASK`).",
            "Implement bare-metal CAN transmission and interrupt-driven reception routines."
        ],
        "prerequisites": "CAN Protocol Fundamentals, S32K144 Memory Map, Embedded C, NVIC Interrupts.",
        "core_concept": "The FlexCAN controller offloads 100% of the low-level bit-stuffing, CRC calculation, frame acknowledgement, and error frame recovery from the ARM Cortex-M4 CPU core. Software interacts with FlexCAN purely through high-level **Message Buffers (MBs)** in RAM: you write an ID and payload into a Transmit MB and set the code to `TX_ONCE`; the hardware transmits the frame onto the CAN bus and generates an interrupt when finished.",
        "lecture_notes": "Lecture 5 and 6 of Embedded System Design and Lab Session 3 covered FlexCAN on the S32K144. Prof. Shree Prasad M. explained: 'FlexCAN has up to 64 Message Buffers located in dedicated internal RAM starting at offset $0\\text{x}0080$. Each MB contains a Control/Status word, 32-bit ID register, and data payload bytes.' The instructor demonstrated configuring FlexCAN in Freeze Mode, setting up the 500 kbps bit timing table, and implementing an interrupt handler to read incoming brake and speed frames.",
        "extra_explanation": "Let's analyze the **FlexCAN Message Buffer & Register Architecture**:\n\n1. **Message Buffer (MB) Structure (16 Bytes per MB in Classic CAN):**\n   - **Word 0 (Offset $+0\\text{x}0$): Control and Status (CS):**\n     - **CODE Field (Bits 27-24):** Indicates MB state:\n       - Transmit Codes: `0b1000` (`TX_INACTIVE`), `0b1100` (`TX_ONCE` - triggers transmission).\n       - Receive Codes: `0b0100` (`RX_EMPTY` - ready to receive), `0b0010` (`RX_FULL` - message received).\n     - **IDE (Bit 21):** ID Extended ($0 = \\text{Standard 11-bit}$, $1 = \\text{Extended 29-bit}$).\n     - **RTR (Bit 20):** Remote Transmission Request.\n     - **DLC (Bits 19-16):** Data Length Code ($0$ to $8$ bytes).\n   - **Word 1 (Offset $+0\\text{x}4$): ID Field:** Standard ID in bits 28-18 (for 11-bit ID: `ID << 18`).\n   - **Words 2 & 3 (Offset $+0\\text{x}8, +0\\text{xC}$):** 8 Data payload bytes.\n\n2. **FlexCAN Initialization Sequence (Freeze Mode):**\n   - Step 1: Enable clock in PCC (`PCC->PCCn[PCC_FlexCAN0_INDEX] |= PCC_PCCn_CGC_MASK`).\n   - Step 2: Request Freeze Mode (`CAN0->MCR |= CAN_MCR_MDIS_MASK;` then clear MDIS and assert `FRZ` & `HALT`). Wait for `FRZACK` bit to set.\n   - Step 3: Configure Bit Timing in `CAN0->CTRL1` (set nominal bit rate to 500 kbps).\n   - Step 4: Initialize Message Buffers (set MB0 to `RX_EMPTY`, MB1 to `TX_INACTIVE`).\n   - Step 5: Exit Freeze Mode by clearing `HALT` and `FRZ` bits in `MCR`.",
        "workflow_steps": [
            ("Enter Freeze Mode", "Assert FRZ & HALT bits in CAN0->MCR; poll FRZACK"),
            ("Bit Timing Calculation", "Set CAN0->CTRL1 (PRESDIV, PROPSEG, PSEG1, PSEG2) for 500 kbps"),
            ("Configure RX Message Buffer", "Set MB0 ID=0x120, IDE=0, CODE=0b0100 (RX_EMPTY)"),
            ("Configure TX Message Buffer", "Set MB1 ID=0x300, IDE=0, CODE=0b1000 (TX_INACTIVE)"),
            ("Exit Freeze Mode & Transmit", "Clear HALT in MCR; write data payload to MB1; set CODE=0b1100 (TX_ONCE)")
        ],
        "diagram_ascii": """
+-----------------------------------------------------------------------------------+
|               NXP S32K144 FLEXCAN MESSAGE BUFFER RAM STRUCTURE                    |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|    MESSAGE BUFFER n (Located in FlexCAN Dedicated RAM: 0x40024080 + n*0x10)       |
|    +--------+----+----+----+----------------------------------------------------+ |
|    | Offset | 31 | 30 | 29 | 28  27  26  25  24 | 21  | 20  | 19  18  17  16    | |
|    +--------+----+----+----+--------------------+-----+-----+-------------------+ |
|    | +0x0   | -  | -  | -  |    CODE (4-bit)    | IDE | RTR |    DLC (4-bit)    | |
|    +--------+----+----+----+--------------------+-----+-----+-------------------+ |
|    | +0x4   | PRIO | Standard ID (Bits 28-18)   | Extended ID (Bits 17-0)       | |
|    +--------+------+----------------------------+-------------------------------+ |
|    | +0x8   | Data Byte 0 | Data Byte 1         | Data Byte 2 | Data Byte 3     | |
|    +--------+-------------+---------------------+-------------+-----------------+ |
|    | +0xC   | Data Byte 4 | Data Byte 5         | Data Byte 6 | Data Byte 7     | |
|    +--------+-------------+---------------------+-------------+-----------------+ |
|                                                                                   |
|    Code States:                                                                   |
|      0b0100 = RX_EMPTY (Ready to receive message)                                 |
|      0b0010 = RX_FULL  (New frame in buffer, CPU must read)                       |
|      0b1100 = TX_ONCE  (Transmit frame once onto CAN bus)                         |
|                                                                                   |
+-----------------------------------------------------------------------------------+
""",
        "working_principle": "Bit Timing Calculation for 500 kbps:\nGiven a $40\\text{ MHz}$ CAN Protocol Clock ($f_{canclk}$):\n- Total Time Quanta per bit ($N_Q$) = $1 + \\text{SyncSeg} + \\text{PropSeg} + \\text{PhaseSeg1} + \\text{PhaseSeg2} = 1 + 1 + 6 + 4 + 4 = 16\\text{ TQ}$.\n- Desired Bit Rate = $500\\text{ kbps} \\implies T_{bit} = 2.0\\ \\mu\\text{s}$.\n- Time Quantum duration $T_Q = \\frac{T_{bit}}{N_Q} = \\frac{2.0\\ \\mu\\text{s}}{16} = 125\\text{ ns}$.\n- Prescaler $\\text{PRESDIV} = \\frac{f_{canclk}}{1 / T_Q} = \\frac{40\\text{ MHz}}{8\\text{ MHz}} = 5 \\implies \\mathbf{\\text{PRESDIV} = 4}$ (0-indexed in register).",
        "automotive_application": "Automotive Powertrain CAN Gateway Routing: The S32K144 FlexCAN0 receives engine RPM and vehicle speed broadcast frames on ID $0\\text{x}100$ every 10 ms. The FlexCAN hardware automatically filters and stores the frame in MB0, raising an interrupt. The ARM core extracts the speed payload and transmits an adjusted target suspension damping command onto FlexCAN1 (Chassis CAN) via MB4 in under $50\\ \\mu\\text{s}$.",
        "comparison_table": {
            "headers": ["Feature / Metric", "Classic CAN 2.0B (FlexCAN)", "CAN-FD (FlexCAN-FD)", "LIN 2.2"],
            "rows": [
                ["Max Data Payload", "8 Bytes per frame", "Up to 64 Bytes per frame", "8 Bytes"],
                ["Max Baud Rate", "1 Mbps (Typically 500 kbps)", "5 Mbps (Fast data phase) / 8 Mbps", "20 kbps"],
                ["Hardware Buffers", "Up to 64 Message Buffers", "Up to 32 (64-byte payload MBs)", "Single byte UART buffer"],
                ["Error Detection", "15-bit CRC + Bit Monitoring + Form Check", "17-bit / 21-bit CRC + Stuff Count", "8-bit Classic Checksum"],
                ["Automotive Domain", "Powertrain, ABS/ESP, Body Control", "ADAS Radar, EV Inverter Telemetry, Flashing", "Door switches, mirrors, wipers, climate"]
            ]
        },
        "formulas": [
            {
                "name": "CAN Bit Rate and Prescaler Formula",
                "math": "\\text{Bit Rate} = \\frac{f_{canclk}}{(\\text{PRESDIV} + 1) \\times (1 + \\text{PROPSEG} + \\text{PSEG1} + \\text{PSEG2} + 3)}",
                "vars": [
                    "f_canclk = Input clock frequency to FlexCAN module (e.g., 40 MHz)",
                    "PRESDIV = Clock prescaler division value (0 to 255)",
                    "PROPSEG, PSEG1, PSEG2 = Segment lengths in time quanta"
                ],
                "example": "With f_canclk = 40 MHz, PRES_DIV = 4 (div by 5), PROPSEG = 5, PSEG1 = 3, PSEG2 = 3 (Total 16 TQ): Bit Rate = 40,000,000 / (5 × 16) = 40,000,000 / 80 = 500,000 bps (500 kbps)."
            }
        ],
        "code_snippet": """// S32K144 Bare-Metal FlexCAN Transmit Message Routine
#include "S32K144.h"

void flexcan_transmit_frame(uint32_t standard_id, uint8_t* data, uint8_t dlc) {
    // Use Message Buffer 1 (MB1) for Transmit
    volatile uint32_t* mb1 = (volatile uint32_t*)&(CAN0->RAMn[1 * 4]);
    
    // 1. Set MB1 Code to TX_INACTIVE (0b1000) to prepare buffer
    mb1[0] = (0x8 << 24);
    
    // 2. Set Standard ID (Bits 28-18)
    mb1[1] = (standard_id & 0x7FF) << 18;
    
    // 3. Load Data Payload Bytes
    mb1[2] = ((uint32_t)data[0] << 24) | ((uint32_t)data[1] << 16) | 
             ((uint32_t)data[2] << 8)  | ((uint32_t)data[3]);
    mb1[3] = ((uint32_t)data[4] << 24) | ((uint32_t)data[5] << 16) | 
             ((uint32_t)data[6] << 8)  | ((uint32_t)data[7]);
             
    // 4. Start Transmission: Set CODE = 0b1100 (TX_ONCE), IDE=0, DLC
    mb1[0] = (0xC << 24) | ((dlc & 0x0F) << 16);
}""",
        "must_remember": [
            "FlexCAN supports up to 64 hardware Message Buffers in dedicated RAM (0x40024080).",
            "To configure bit rates, FlexCAN MUST be placed into Freeze Mode (FRZ & HALT).",
            "Standard 11-bit CAN ID is placed in bits 28-18 of Word 1 (`ID << 18`).",
            "TX_ONCE code (`0b1100`) triggers automatic autonomous hardware frame transmission.",
            "CAN-FD supports up to 64-byte payloads at data bitrates up to 5-8 Mbps."
        ],
        "short_qa": [
            ("What are the two steps required to put the S32K144 FlexCAN controller into Freeze Mode for configuration?", "Step 1: Set the `FRZ` (Freeze Enable) and `HALT` bits in the Module Configuration Register (`CAN0->MCR`). Step 2: Poll the `FRZACK` (Freeze Acknowledge) bit in `CAN0->MCR` until hardware asserts it high, confirming that the CAN state machine is frozen."),
            ("What is the difference between Message Buffer Code `0b0100` and `0b0010` during FlexCAN reception?", "Code `0b0100` (`RX_EMPTY`) configures the Message Buffer as active and waiting to receive an incoming CAN frame. Code `0b0010` (`RX_FULL`) is set automatically by hardware when a matching CAN frame has been received and written into the buffer, signaling the CPU to read the payload.")
        ],
        "long_qa": [
            ("Explain the architecture and memory layout of Message Buffers in the NXP S32K144 FlexCAN module. Detail the bitfields of Word 0 (Control/Status) and Word 1 (ID). Calculate the register timing parameters to achieve a 500 kbps bit rate from a 40 MHz CAN clock.", "A complete answer covers: (1) FlexCAN RAM memory map diagram from offset 0x0080; (2) Detailed bitfield diagram of Word 0 (CODE, IDE, RTR, DLC, TIMESTAMP) and Word 1 (Standard/Extended ID); (3) Explanation of RX_EMPTY, RX_FULL, TX_INACTIVE, and TX_ONCE codes; (4) Step-by-step bit timing derivation showing TQ=16, PRES_DIV=4, PROPSEG=5, PSEG1=3, PSEG2=3 to achieve exactly 500 kbps from 40 MHz clock.")
        ],
        "viva_interview_qa": [
            ("Why does the CPU have to read the Timer Free-Running Register (`CAN0->TIMER`) after reading a received Message Buffer payload in an ISR?", "Reading the `CAN0->TIMER` register unlocks the Message Buffer RAM array in hardware. If the software reads the MB payload but forgets to read `CAN0->TIMER`, the FlexCAN controller keeps the internal buffer locked, preventing new incoming CAN frames from being received in that buffer.")
        ],
        "common_mistakes": [
            "Writing the 11-bit CAN Standard ID starting at bit 0 instead of bit 18. In FlexCAN, Standard IDs MUST be shifted left by 18 bits (`ID << 18`).",
            "Attempting to write to `CAN0->CTRL1` while the controller is running outside Freeze Mode. Timing registers are write-protected outside Freeze Mode."
        ],
        "revision_points": [
            "64 MBs in RAM at 0x40024080.",
            "Freeze Mode (FRZ + HALT) required to change bit timing.",
            "Standard ID shifted by 18 bits: ID << 18.",
            "TX_ONCE = 0b1100 triggers transmission.",
            "Read CAN0->TIMER to unlock MB after RX."
        ],
        "sources": "Embedded System Design Lecture 5 & 6 Transcripts; S32K144 Reference Manual Chapter 53 (FlexCAN); ESD Lab 3 Manual."
    }
]

def append_topics(filepath, new_topics):
    content = filepath.read_text(encoding='utf-8')
    idx = content.rfind(']')
    if idx == -1:
        print(f"Error: Could not find closing bracket in {filepath}")
        return
    topics_str = ""
    for t in new_topics:
        topics_str += ",\n" + pprint.pformat(t, width=100, sort_dicts=False)
    new_content = content[:idx] + topics_str + "\n]" + content[idx+1:]
    filepath.write_text(new_content, encoding='utf-8')
    print(f"Appended {len(new_topics)} topics to {filepath.name}")

if __name__ == '__main__':
    append_topics(TOOLS_DIR / "data_av.py", AV_TOPICS_2)
    append_topics(TOOLS_DIR / "data_at.py", AT_TOPICS_2)
    append_topics(TOOLS_DIR / "data_esd.py", ESD_TOPICS_2)
