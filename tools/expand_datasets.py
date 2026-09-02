"""Appends rich textbook-grade topics for Automotive Vehicle, Autotronics, and Embedded System Design."""
import sys
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parent

# --- Extra Automotive Vehicle Topics ---
AV_EXTRA_TOPICS = [
    {
        "slug": "engine-performance-parameters",
        "title": "Engine Performance Parameters: Power, Torque & BSFC",
        "module": "IC Engine Fundamentals",
        "level": "Intermediate",
        "importance": 5,
        "overview": "Evaluating the performance of internal combustion engines requires standardized mechanical, thermal, and volumetric parameters. Key metrics include Indicated Power (IP), Brake Power (BP), Mechanical Efficiency (η_mech), Brake Specific Fuel Consumption (BSFC), Mean Effective Pressure (IMEP/BMEP), and Volumetric Efficiency (η_v).",
        "learning_objectives": [
            "Differentiate between Indicated Power (IP) developed in cylinder and Brake Power (BP) delivered at crankshaft.",
            "Calculate Brake Specific Fuel Consumption (BSFC) and interpret engine BSFC 'island' contour maps.",
            "Understand Mean Effective Pressure (BMEP and IMEP) as size-independent engine metrics.",
            "Explain Volumetric Efficiency (η_v) and techniques to exceed 100% using turbocharging and tuned intake runners."
        ],
        "prerequisites": "IC Engine 4-Stroke Thermodynamic Cycles, Work and Power Physics.",
        "core_concept": "Not all energy released by burning fuel reaches the car's wheels. The hot expanding gas inside the cylinder develops Indicated Power (IP). But as the piston rubs against cylinder walls, bearings spin in oil, and camshafts open heavy valves, friction and pumping losses consume a portion (Friction Power, FP). What remains at the flywheel is Brake Power (BP = IP - FP).",
        "lecture_notes": "Lecture 6 and Session 6 covered engine performance testing. The professor highlighted: 'BSFC is the ultimate measure of how efficiently an engine turns fuel into shaft work. The lower the BSFC, the more efficient the engine.' The lecturer walked through engine dyno testing procedures (Morse test, eddy-current dynamometers) and explained how BMEP allows comparing a 1.0L 3-cylinder engine directly against a 6.0L V8.",
        "extra_explanation": "Let's analyze the governing mathematical definitions:\n\n1. **Power Relationships:**\n   $$IP = BP + FP, \\quad \\eta_{mech} = \\frac{BP}{IP} = \\frac{BP}{BP + FP}$$\n   - **Indicated Power (IP):** $IP = \\frac{P_{imep} \\cdot L \\cdot A \\cdot N_{power} \\cdot k}{60}$, where $N_{power} = N/2$ for 4-stroke engines, $k$ = number of cylinders.\n   - **Brake Power (BP):** $BP = \\frac{2\\pi N T}{60} = \\omega \\cdot T$, where $T$ is brake torque measured by a dynamometer (N·m) and $N$ is engine RPM.\n\n2. **Brake Mean Effective Pressure (BMEP):**\n   $$BMEP = \\frac{BP \\times 60 \\times n_R}{V_d \\times N} = \\frac{2\\pi \\cdot n_R \\cdot T}{V_d}$$\n   - For 4-stroke ($n_R = 2$), $BMEP = \\frac{4\\pi T}{V_d}$. Notice that BMEP is directly proportional to engine torque normalized by displacement volume $V_d$!\n\n3. **Brake Specific Fuel Consumption (BSFC):**\n   $$BSFC = \\frac{\\dot{m}_f}{BP} \\quad \\left[\\frac{\\text{g}}{\\text{kWh}}\\right]$$\n   - Where $\\dot{m}_f$ is fuel mass flow rate (g/h). Typical modern gasoline engines achieve a sweet spot of $230 - 250\\text{ g/kWh}$ (approx. $34-37\\%$ thermal efficiency), while heavy-duty diesels reach $190 - 210\\text{ g/kWh}$ ($42-46\\%$ efficiency).",
        "workflow_steps": [
            ("Dynamometer Load Test", "Engine mounted on test bench; dyno applies braking torque T at RPM N"),
            ("Brake Power Calculation", "BP = (2 * pi * N * T) / 60 computed directly from torque and speed"),
            ("Fuel Consumption Gravimetric Weighing", "Mass flow rate m_dot_f (kg/h) measured via precision flow meter"),
            ("BSFC Computation", "BSFC = m_dot_f / BP determines specific fuel economy"),
            ("Friction Power Determination", "Morse test or motoring method determines FP; calculates IP = BP + FP")
        ],
        "diagram_ascii": """
+-----------------------------------------------------------------------------------+
|               ENGINE POWER FLOW & BSFC EFFICIENCY MAP                             |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|    Total Fuel Heat Energy Input (m_dot_f * Calorific Value)                       |
|         |                                                                         |
|         +-----> Cooling Water & Radiator Losses (~30%)                            |
|         +-----> Exhaust Gas Heat Losses (~35%)                                    |
|         |                                                                         |
|         v                                                                         |
|    INDICATED POWER (IP) [Work done inside cylinder = 100%]                        |
|         |                                                                         |
|         +-----> Pumping Losses (Intake suction & exhaust pumping)                 |
|         +-----> Piston Ring & Bearing Friction Losses                             |
|         +-----> Valvetrain & Oil/Water Pump Drive Losses                          |
|         |       (Total Friction Power FP ≈ 10-18%)                                |
|         v                                                                         |
|    BRAKE POWER (BP = IP - FP) [Delivered to Flywheel ≈ 82-90% of IP]              |
|                                                                                   |
+-----------------------------------------------------------------------------------+
""",
        "working_principle": "Volumetric Efficiency (η_v) and Forced Induction:\nVolumetric efficiency measures how effectively the cylinder fills with fresh air during the intake stroke: $\\eta_v = \\frac{\\dot{m}_{air, actual}}{\\rho_{air, ambient} \\cdot V_d \\cdot (N/2)}$. Naturally aspirated engines suffer intake throttling and flow friction, limiting $\\eta_v$ to $80-90\\%$. Turbochargers and superchargers compress intake air to $1.5 - 2.5\\text{ bar}$ absolute pressure, pushing $\\eta_v$ to **$150\\% - 220\\%$**, allowing a downsized 1.5L turbo engine to produce the torque of a 3.0L naturally aspirated engine.",
        "automotive_application": "BSFC Sweet-Spot Operating Point in Hybrid Powertrains: In a Toyota Hybrid System (THS-II), the planetary power-split device decouples engine speed from vehicle road speed. The hybrid control ECU continuously adjusts engine RPM and torque to force the gasoline engine to run strictly inside its lowest-BSFC island ($225\\text{ g/kWh}$ at 2200 RPM / 120 Nm), using the electric motor/generator to absorb excess power or provide boost.",
        "comparison_table": {
            "headers": ["Parameter", "Symbol / Unit", "Physical Meaning", "Typical Value (Gasoline)"],
            "rows": [
                ["Brake Power", "BP (kW)", "Net usable shaft power delivered at engine flywheel", "75 to 250 kW"],
                ["Indicated Power", "IP (kW)", "Total mechanical power generated by gas pressure on pistons", "90 to 290 kW"],
                ["Mechanical Efficiency", "η_mech (%)", "Ratio of Brake Power to Indicated Power (BP/IP)", "82% to 90%"],
                ["BMEP", "bar / kPa", "Mean effective pressure delivered over expansion stroke", "9 to 14 bar (NA) / 18 to 28 bar (Turbo)"],
                ["BSFC", "g / kWh", "Grams of fuel consumed per kilowatt-hour of shaft work", "230 to 270 g/kWh (Peak sweet spot)"]
            ]
        },
        "formulas": [
            {
                "name": "Brake Power Formula",
                "math": "BP = \\frac{2\\pi \\cdot N \\cdot T}{60000} \\quad [\\text{kW}]",
                "vars": [
                    "N = Engine crankshaft rotational speed (RPM)",
                    "T = Engine brake torque (N·m)",
                    "60000 = Conversion factor from W to kW and minutes to seconds"
                ],
                "example": "An engine develops T = 250 N·m torque at N = 4000 RPM. Brake power is BP = (2 × 3.14159 × 4000 × 250) / 60000 = 6,283,185 / 60000 = 104.72 kW (140.4 HP)."
            },
            {
                "name": "Brake Specific Fuel Consumption (BSFC)",
                "math": "BSFC = \\frac{\\dot{m}_f \\times 1000}{BP} \\quad \\left[\\frac{\\text{g}}{\\text{kWh}}\\right]",
                "vars": [
                    "\\dot{m}_f = Fuel consumption rate (kg/h)",
                    "BP = Brake power output (kW)"
                ],
                "example": "If the engine above consumes 26.0 kg of gasoline per hour while delivering 104.72 kW: BSFC = (26.0 × 1000) / 104.72 = 248.28 g/kWh."
            }
        ],
        "code_snippet": """// C Engine Performance Metric Calculator
#include <stdio.h>

void calculate_engine_metrics(double torque_nm, double rpm, double fuel_kg_hr, double displacement_litres) {
    double bp_kw = (2.0 * 3.14159265 * rpm * torque_nm) / 60000.0;
    double bsfc = (fuel_kg_hr * 1000.0) / bp_kw;
    // BMEP = (4 * pi * T) / Vd  [in bar: 1 bar = 100,000 Pa]
    double v_d_m3 = displacement_litres * 1e-3;
    double bmep_bar = ((4.0 * 3.14159265 * torque_nm) / v_d_m3) / 100000.0;
    
    printf("--- ENGINE DYNAMOMETER REPORT ---\\n");
    printf("Brake Power : %6.2f kW (%5.1f HP)\\n", bp_kw, bp_kw * 1.341);
    printf("BSFC        : %6.2f g/kWh\\n", bsfc);
    printf("BMEP        : %6.2f bar\\n", bmep_bar);
}""",
        "must_remember": [
            "Brake Power BP = (2 * pi * N * T) / 60000 (kW).",
            "Indicated Power IP = BP + FP; Mechanical efficiency η_mech = BP / IP.",
            "BSFC = fuel mass flow rate / Brake Power (g/kWh); lower is more efficient.",
            "BMEP is proportional to Torque / Displacement; allows comparing engines of different sizes."
        ],
        "short_qa": [
            ("What is the difference between Indicated Power (IP) and Brake Power (BP)?", "Indicated Power is the total theoretical power generated inside the engine cylinders by the combustion pressure acting on the pistons. Brake Power is the actual usable mechanical power delivered at the engine crankshaft/flywheel after subtracting internal friction and pumping losses (BP = IP - FP)."),
            ("Why is Brake Mean Effective Pressure (BMEP) considered a better metric than peak torque for comparing engine designs?", "Peak torque depends directly on engine displacement size (a 5.0L engine naturally makes more torque than a 1.0L engine). BMEP normalizes torque by engine displacement volume, measuring how effectively the engine extracts work per unit volume regardless of engine size.")
        ],
        "long_qa": [
            ("Define Indicated Power, Brake Power, Friction Power, Mechanical Efficiency, and BSFC. A 4-cylinder 4-stroke 2.0L engine running at 4500 RPM produces a dynamometer torque of 220 N·m while consuming 24.5 kg/h of fuel. Calculate its Brake Power, BMEP, and BSFC.", "A complete answer covers: (1) Definitions and physical formulas for IP, BP, FP, η_mech, and BSFC; (2) Calculation of BP = (2*pi*4500*220)/60000 = 103.67 kW; (3) Calculation of BMEP = (4*pi*220) / (0.002) / 100000 = 13.82 bar; (4) Calculation of BSFC = (24.5*1000) / 103.67 = 236.33 g/kWh; (5) Explanation of BSFC contour map.")
        ],
        "viva_interview_qa": [
            ("How does the Morse Test determine the Indicated Power (IP) of a multi-cylinder engine without using cylinder pressure transducers?", "The engine is run at a steady RPM on a dynamometer with all cylinders firing, measuring total Brake Power ($BP_{total}$). Then, one cylinder's spark plug or injector is cut off, and the dyno load is adjusted to bring speed back to the exact same RPM, measuring the new Brake Power ($BP_{-1}$). The Indicated Power of the cut cylinder is $IP_1 = BP_{total} - BP_{-1}$. Repeating this for all cylinders gives total $IP = \\sum IP_i$.")
        ],
        "common_mistakes": [
            "Forgetting the factor of $60000$ when calculating Brake Power in kW from RPM and N·m.",
            "Assuming lower BSFC means worse fuel economy. BSFC is fuel consumed per unit work; **lower BSFC means higher fuel efficiency**."
        ],
        "revision_points": [
            "BP = 2 * pi * N * T / 60000.",
            "IP = BP + FP.",
            "BSFC = m_dot_f / BP (g/kWh).",
            "BMEP = 4*pi*T / V_d (4-stroke)."
        ],
        "sources": "Automotive Vehicle Lecture 6 Transcript; Session 6 IC Engines PDF; Syllabus Section 4."
    },
    {
        "slug": "transmission-systems-and-gearboxes",
        "title": "Transmission Systems: MT, AT, DCT, CVT & Planetary Gearsets",
        "module": "Powertrain Fundamentals",
        "level": "Intermediate",
        "importance": 5,
        "overview": "Internal combustion engines produce useful torque only across a narrow speed range (1500 to 6000 RPM) and cannot start under zero-RPM load. The transmission system adapts high engine speed / low torque to high wheel torque / low speed for launching, hill climbing, and high-speed cruising. Modern automotive transmissions include Manual (MT), Automatic with Hydraulic Torque Converter (AT), Dual-Clutch (DCT), Continuously Variable (CVT), and Epicyclic Planetary Gearsets.",
        "learning_objectives": [
            "Explain why multi-ratio transmissions are required for internal combustion engines.",
            "Analyze the working of manual synchromesh gearboxes and dry friction clutches.",
            "Understand Automatic Transmissions: Fluid Torque Converters, Impeller, Turbine, and Stator one-way clutch.",
            "Analyze Dual-Clutch Transmissions (DCT) and how odd/even pre-selection enables zero-torque-interruption shifts.",
            "Derive gear ratios for Epicyclic Planetary Gearsets using Willis's formula."
        ],
        "prerequisites": "Powertrain Architectures & Layouts, Tractive Force, Engine Torque-Speed Curves.",
        "core_concept": "An IC engine at 0 RPM produces 0 torque and stalls instantly if connected directly to stationary wheels. A transmission provides two vital functions: a disconnect device (clutch/torque converter) to allow the engine to idle while the car is stopped, and a set of torque-multiplying gear ratios (e.g., 4:1 in 1st gear for launch torque, 0.7:1 in 6th gear for quiet, fuel-efficient highway cruising).",
        "lecture_notes": "Lectures 2 and 3 covered transmission systems. The professor explained: 'Why do we need a gearbox? Because of the tractive effort vs vehicle speed hyperbola. The ideal tractive curve is a constant-power hyperbola ($P = F \\cdot v = \\text{constant}$). The transmission approximates this ideal hyperbola through stepped gear ratios.' The lecturer walked through torque converters, explaining hydrodynamic torque multiplication via the stator redirecting fluid.",
        "extra_explanation": "Let's compare modern automotive transmission technologies:\n\n1. **Manual Transmission (MT) & Dry Friction Clutch:**\n   - Uses a single/twin dry friction clutch disc clamped by a diaphragm spring between flywheel and pressure plate.\n   - Helical gears remain in constant mesh; brass **Synchromesh rings** use friction to match gear and shaft speeds before dog teeth engage, eliminating grinding.\n\n2. **Automatic Transmission (AT) & Hydrodynamic Torque Converter:**\n   - Replaces friction clutch with a sealed fluid coupling containing three elements:\n     - **Impeller (Pump):** Driven by engine crankshaft, flings ATF fluid outward.\n     - **Turbine:** Driven by circulating ATF fluid, connected to gearbox input shaft.\n     - **Stator (with One-Way Sprag Clutch):** Stationary at stall; redirects returning fluid to aid impeller rotation, achieving **Torque Multiplication of $2.0\\text{x} - 2.5\\text{x}$** during vehicle launch.\n     - **Lockup Clutch:** Mechanically locks impeller and turbine together at highway speeds for 100% efficiency.\n\n3. **Dual-Clutch Transmission (DCT):**\n   - Uses two nested concentric clutches (Clutch 1 for Odd gears 1, 3, 5, 7; Clutch 2 for Even gears 2, 4, 6, R).\n   - While driving in 2nd gear on Clutch 2, the transmission computer pre-selects 3rd gear on the disengaged Clutch 1 shaft. Shifting occurs by cross-fading the two clutches in $15 - 40\\text{ ms}$ with **zero power interruption**.\n\n4. **Continuously Variable Transmission (CVT):**\n   - Uses two variable-diameter split-cone pulleys connected by a steel push-belt. Moving the conical sheaves hydraulically changes the belt radius continuously, providing infinite gear ratios between minimum and maximum bounds ($i_{max} \\approx 2.6, i_{min} \\approx 0.45$).\n\n5. **Epicyclic Planetary Gearset (Willis Formula):**\n   - Consists of a central **Sun gear ($S$)**, multiple **Planet gears ($P$)** on a **Planet Carrier ($C$)**, and an outer **Ring / Annulus gear ($R$)**.\n   - Fundamental Kinematic Equation: $\\frac{\\omega_S - \\omega_C}{\\omega_R - \\omega_C} = -\\frac{N_R}{N_S}$",
        "workflow_steps": [
            ("Engine Torque Input", "Engine drives torque converter impeller or clutch basket"),
            ("Hydrodynamic Multiplication", "Torque converter multiplies stall torque 2.2x to launch vehicle"),
            ("Electronic TCU Shift Decision", "Transmission Control Unit monitors TPS angle and vehicle speed"),
            ("Hydraulic Valve Body Actuation", "Solenoids modulate hydraulic pressure to apply multi-plate clutch packs"),
            ("Planetary Ratio Selection", "Clutch packs lock sun/ring gears to select forward/reverse ratios")
        ],
        "diagram_ascii": """
+-----------------------------------------------------------------------------------+
|               AUTOMATIC TORQUE CONVERTER & EPICYCLIC PLANETARY GEARSET            |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|    1. TORQUE CONVERTER HYDRODYNAMICS                                              |
|       +------------------------------------------------------------------+        |
|       |  Engine Crankshaft ===> [ IMPELLER ] --- Fluid Vortex --->       |        |
|       |                                                                  |        |
|       |                         [ STATOR ] (One-Way Sprag Clutch)        |        |
|       |                         (Redirects returning fluid to multiply   |        |
|       |                          torque 2.2x at launch)                  |        |
|       |                                                                  |        |
|       |       <--- Returning Fluid --- [ TURBINE ] ===> Input Shaft      |        |
|       +------------------------------------------------------------------+        |
|                                                                                   |
|    2. EPICYCLIC PLANETARY GEARSET                                                 |
|                  +-----------------------------------+                            |
|                  |          RING GEAR (R)            |                            |
|                  |   +---------------------------+   |                            |
|                  |   |    (P)             (P)    |   |                            |
|                  |   |   Planet          Planet  |   |                            |
|                  |   |   +---+           +---+   |   |                            |
|                  |   |   |   |  [ SUN ]  |   |   |   |                            |
|                  |   |   +---+  (S Gear) +---+   |   |                            |
|                  |   |    (P)   Carrier   (P)    |   |                            |
|                  |   |          (C)              |   |                            |
|                  |   +---------------------------+   |                            |
|                  +-----------------------------------+                            |
|                                                                                   |
+-----------------------------------------------------------------------------------+
""",
        "working_principle": "Planetary Gearset Ratio Selection Rules:\n- **Underdrive / Reduction (1st Gear):** Hold Ring stationary (brake applied), Drive Sun gear $\\to$ Carrier rotates slowly with high multiplied torque: $\\frac{\\omega_{in}}{\\omega_{out}} = 1 + \\frac{N_R}{N_S}$.\n- **Overdrive (High Gear):** Hold Sun stationary, Drive Carrier $\\to$ Ring rotates faster than input: $\\frac{\\omega_{in}}{\\omega_{out}} = \\frac{1}{1 + N_S/N_R} < 1.0$.\n- **Reverse Gear:** Hold Carrier stationary, Drive Sun $\\to$ Ring rotates in opposite direction: $\\frac{\\omega_{in}}{\\omega_{out}} = -\\frac{N_R}{N_S}$.",
        "automotive_application": "Toyota Prius Hybrid Synergy Drive (HSD): The engine is connected directly to the Planet Carrier ($C$), the smaller Motor/Generator (MG1) is connected to the Sun gear ($S$), and the traction Motor (MG2) and wheels are connected to the Ring gear ($R$). By electronically controlling the speed and direction of MG1, the planetary gearset acts as an Electronic Continuously Variable Transmission (e-CVT) without any belts, clutches, or hydraulics.",
        "comparison_table": {
            "headers": ["Transmission Type", "Clutch / Coupling", "Shift Mechanism", "Efficiency", "Driving Character"],
            "rows": [
                ["Manual (MT)", "Single dry friction disc", "Mechanical fork & synchromesh", "95% - 97% (High)", "Direct driver engagement, clutch pedal required"],
                ["Automatic (AT)", "Hydraulic Torque Converter", "Planetary gearsets + Hydraulic clutches", "86% - 92% (Lockup helps)", "Smooth creep, seamless automatic shifts"],
                ["Dual-Clutch (DCT)", "Dual wet or dry clutches", "Odd/even pre-selected parallel shafts", "93% - 96% (High)", "Ultra-fast lightning shifts (20ms), sporty feel"],
                ["CVT (Continuously Variable)", "Torque converter or wet clutch", "Variable conical pulleys + steel push belt", "85% - 90% (Moderate)", "Rubber-band RPM effect, optimal steady fuel economy"],
                ["EV Single-Speed", "None (Direct splined shaft)", "Fixed helical reduction gear (e.g., 9:1)", "97% - 98% (Highest)", "Instant torque from 0 RPM, zero shift delays"]
            ]
        },
        "formulas": [
            {
                "name": "Planetary Gear Ratio (Willis Kinematic Formula)",
                "math": "\\frac{\\omega_S - \\omega_C}{\\omega_R - \\omega_C} = -\\frac{N_R}{N_S}",
                "vars": [
                    "\\omega_S, \\omega_R, \\omega_C = Angular velocities of Sun, Ring, and Carrier",
                    "N_S = Number of teeth on Sun gear (e.g., 30 teeth)",
                    "N_R = Number of teeth on Ring gear (e.g., 90 teeth)"
                ],
                "example": "If Ring is held fixed (ω_R = 0) with N_S = 30 and N_R = 90: (ω_S - ω_C) / (0 - ω_C) = -90/30 = -3. ω_S - ω_C = 3 ω_C -> ω_S = 4 ω_C. Gear ratio is ω_in / ω_out = ω_S / ω_C = 4.0:1 reduction."
            }
        ],
        "code_snippet": """// Python Planetary Gearset Kinematic Ratio Solver
def planetary_gear_ratios(teeth_sun=30, teeth_ring=90):
    k = teeth_ring / teeth_sun  # Typically 2.0 to 4.0
    
    # Mode 1: Hold Ring (Forward 1st Gear)
    ratio_forward_1 = 1.0 + k
    # Mode 2: Hold Sun (Forward Overdrive)
    ratio_overdrive = 1.0 / (1.0 + (1.0 / k))
    # Mode 3: Hold Carrier (Reverse Gear)
    ratio_reverse = -k
    
    print(f"Planetary (Sun={teeth_sun}T, Ring={teeth_ring}T, Ratio k={k:.1f}):")
    print(f"  Hold Ring    -> 1st Gear Reduction : {ratio_forward_1:.2f} : 1")
    print(f"  Hold Sun     -> Overdrive Ratio    : {ratio_overdrive:.2f} : 1")
    print(f"  Hold Carrier -> Reverse Gear Ratio : {ratio_reverse:.2f} : 1")

planetary_gear_ratios(30, 90)""",
        "must_remember": [
            "Transmissions match narrow engine torque curves to wide vehicle road speed requirements.",
            "Torque converters provide fluid coupling and multiply torque up to 2.5x via the stationary stator.",
            "DCT uses twin clutches (odd/even) for millisecond shifts without torque interruption.",
            "CVT uses variable conical pulleys for continuously variable ratio matching.",
            "Willis planetary formula: (ω_S - ω_C) / (ω_R - ω_C) = -N_R / N_S."
        ],
        "short_qa": [
            ("What is the function of the stator in an automotive hydraulic torque converter?", "The stator redirects the fluid returning from the turbine back into the impeller at an assisting angle rather than an opposing angle. This hydrodynamic fluid redirection multiplies engine input torque by a factor of 2.0x to 2.5x during vehicle launch from a standstill."),
            ("How does a Dual-Clutch Transmission (DCT) achieve gear shifts without torque interruption?", "A DCT features two separate input shafts driven by two independent clutches—one for odd gears (1, 3, 5, 7) and one for even gears (2, 4, 6, R). While accelerating in one gear, the transmission controller pre-engages the next gear on the idle shaft; the shift is executed by simultaneously disengaging one clutch while engaging the other in milliseconds.")
        ],
        "long_qa": [
            ("Explain the construction and working principle of a modern automatic transmission torque converter. Include the impeller, turbine, stator, and lockup clutch with a fluid circulation diagram. Derive the planetary gear reduction ratio when the ring gear is held stationary.", "A complete answer covers: (1) Cross-sectional diagram of torque converter; (2) Hydrodynamic working of impeller, turbine, and stator; (3) Explanation of torque multiplication at stall vs 1:1 coupling at speed; (4) Lockup clutch operation; (5) Application of Willis formula to derive 1st gear reduction ratio i = 1 + (N_R / N_S).")
        ],
        "viva_interview_qa": [
            ("Why do pure Electric Vehicles (EVs) like the Tesla Model 3 only require a single-speed reduction gearbox instead of a 6-speed or 8-speed transmission?", "Electric traction motors produce 100% maximum torque right from 0 RPM and can spin smoothly up to 18,000–20,000 RPM. This broad, linear torque-speed capability spans the entire vehicle speed range (0 to 250 km/h) with a simple fixed ~9:1 reduction gear, eliminating the weight, cost, friction, and complexity of a multi-speed transmission.")
        ],
        "common_mistakes": [
            "Thinking a torque converter multiplies torque at all speeds. Torque multiplication occurs ONLY when there is a significant speed differential between impeller and turbine (at vehicle launch). At cruising speeds, torque ratio is 1:1.",
            "Confusing the role of the synchromesh ring. The synchromesh matches shaft speeds using friction before dog teeth engage; it does not transmit driving power."
        ],
        "revision_points": [
            "MT = Synchromesh + Dry Clutch.",
            "AT = Torque Converter (Impeller/Turbine/Stator) + Planetary.",
            "DCT = Dual clutches, zero torque interruption.",
            "CVT = Variable cone pulleys + steel belt.",
            "Willis: (ω_S - ω_C)/(ω_R - ω_C) = -N_R/N_S."
        ],
        "sources": "Automotive Vehicle Lecture 2 & 3 Transcripts; Session 3 Powertrain Components PDF; Syllabus Section 3."
    }
]

# --- Extra Autotronics Topics ---
AT_EXTRA_TOPICS = [
    {
        "slug": "operational-amplifiers-in-signal-conditioning",
        "title": "Operational Amplifiers & Sensor Signal Conditioning",
        "module": "Analog Signal Conditioning",
        "level": "Intermediate",
        "importance": 5,
        "overview": "Automotive sensors (piezoelectric knock sensors, thermocouples, strain gauge load cells, and variable reluctance wheel speed sensors) output raw electrical signals in the microvolt or millivolt range, often contaminated by high-voltage electrical noise from the alternator and spark plugs. Operational Amplifiers (Op-Amps) provide amplification, impedance isolation, differential common-mode noise rejection, and active filtering to condition weak sensor signals for microcontroller ADC inputs.",
        "learning_objectives": [
            "Apply the Ideal Op-Amp Golden Rules: Infinite input impedance ($I_+ = I_- = 0$) and Virtual Short ($V_+ = V_-$).",
            "Analyze and design Inverting, Non-Inverting, and Voltage Follower (Buffer) amplifier circuits.",
            "Derive the differential gain equation for Difference Amplifiers and 3-Op-Amp Instrumentation Amplifiers.",
            "Design active Sallen-Key low-pass filters to eliminate high-frequency EMI noise before ADC digitization."
        ],
        "prerequisites": "Circuit Laws (KCL, KVL, Thévenin), Voltage Dividers, Transistors.",
        "core_concept": "An ideal Op-Amp is an analog amplifier with infinite gain, infinite input impedance, and zero output impedance. When connected with negative feedback, two magical 'Golden Rules' emerge: (1) No current flows into either input terminal ($I_{in} = 0$), and (2) The output will do whatever it takes through the feedback loop to force the negative input voltage to equal the positive input voltage ($V_- = V_+$).",
        "lecture_notes": "Lecture 5 of Autotronics covered Op-Amps in signal conditioning. Dr. Madhuri Bayya emphasized: 'Sensors produce millivolt signals that are easily corrupted. If you connect a weak sensor directly to an ADC, the ADC's input impedance loads the sensor and distorts the reading. You must use an Op-Amp buffer or differential amplifier to amplify the signal and reject common-mode ground noise.' The professor derived inverting and non-inverting gain formulas using KCL at the virtual ground summing node.",
        "extra_explanation": "Let's analyze the fundamental Op-Amp configurations:\n\n1. **Inverting Amplifier:**\n   - Positive terminal grounded ($V_+ = 0\\text{ V} \\implies V_- = 0\\text{ V}$, Virtual Ground).\n   - KCL at $V_-$: $\\frac{V_{in} - 0}{R_{in}} + \\frac{V_{out} - 0}{R_f} = 0 \\implies \\mathbf{V_{out} = -\\left(\\frac{R_f}{R_{in}}\\right) V_{in}}$\n\n2. **Non-Inverting Amplifier:**\n   - Input applied to $V_+$ ($V_+ = V_{in} \\implies V_- = V_{in}$).\n   - Voltage divider at feedback path: $V_- = V_{out} \\cdot \\frac{R_1}{R_1 + R_f} = V_{in} \\implies \\mathbf{V_{out} = \\left(1 + \\frac{R_f}{R_1}\\right) V_{in}}$\n   - **Voltage Follower / Buffer ($R_f = 0, R_1 = \\infty$):** $V_{out} = V_{in}$. Provides infinite input impedance (zero sensor loading) and zero output impedance.\n\n3. **Differential Amplifier & Instrumentation Amplifier:**\n   - Eliminates ground offsets and common-mode noise picked up along long vehicle wiring harnesses.\n   - **Difference Amplifier:** $V_{out} = \\frac{R_f}{R_{in}} (V_2 - V_1)$ (when bridge resistors match).\n   - **Three Op-Amp Instrumentation Amplifier (e.g., INA128):**\n     $$V_{out} = \\left(1 + \\frac{2R_1}{R_{gain}}\\right) \\left(\\frac{R_3}{R_2}\\right) (V_2 - V_1)$$\n   - Offers extremely high Common-Mode Rejection Ratio ($CMRR > 110\\text{ dB}$) and gigohm input impedance for thermocouple and bridge sensors.",
        "workflow_steps": [
            ("Raw Sensor Signal", "Thermocouple or Wheatstone bridge outputs weak 5 mV differential signal"),
            ("Buffer Stage (Input Z)", "High input impedance prevents sensor loading error"),
            ("Differential Amplification", "Rejects common-mode alternator ripple noise; amplifies mV to 0-5V"),
            ("Active Low-Pass Filtering", "2nd order Sallen-Key filter attenuates noise above cutoff frequency f_c"),
            ("ADC Sampling", "Clean 0-5V analog voltage sampled by microcontroller ADC")
        ],
        "diagram_ascii": """
+-----------------------------------------------------------------------------------+
|               THREE OP-AMP INSTRUMENTATION AMPLIFIER (SIGNAL CONDITIONING)        |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|    Sensor V1 (+) o-----+                                                          |
|                        |                                                          |
|                     |\ |                                                          |
|                     | \                                                           |
|                     |  \---+----------[ R1 ]---------+                            |
|                     |  /   |                         |                            |
|                  +--|-/    |                         |    R2           R3         |
|                  |  |/     |                       +-+--[   ]--+     +-[   ]-+    |
|                  |         |                       |           |     |       |    |
|                  +-[ R_G ]-+                       |        |\ |     |       |    |
|                  | (Gain)  |                       |        | \      |       |    |
|                  |         |                       +--------|- \-----+       +--> |
|                  +--|-/    |                                |   \            Vout |
|                     |/     |                       +--------|+  /                 |
|                     |  \   |                       |        |  /                  |
|                     |   \--+----------[ R1 ]-------+        |/                    |
|                     |  /   |                       |                              |
|                     | /    |                       +----[ R2 ]----+---[ R3 ]-+    |
|    Sensor V2 (-) o--|/     |                                      |          |    |
|                                                                 =====      =====  |
|                                                                 Ground     Ground |
|                                                                                   |
|    Gain Equation:   Vout = [ 1 + 2*R1 / R_G ] * (R3 / R2) * (V1 - V2)             |
|                                                                                   |
+-----------------------------------------------------------------------------------+
""",
        "working_principle": "Common-Mode Rejection Ratio (CMRR):\nIn an automotive engine bay, ignition sparks and alternator coils radiate high-frequency electromagnetic interference (EMI) that induces identical noise voltages on both sensor signal wires ($V_{noise, 1} = V_{noise, 2} = V_{cm}$). A single-ended amplifier amplifies this noise, corrupting the reading. A **Differential / Instrumentation Amplifier** amplifies ONLY the difference between wires ($V_{diff} = V_1 - V_2$) while rejecting the identical common-mode noise ($V_{cm}$): $\\text{CMRR} = 20 \\log_{10} \\left( \\frac{A_d}{A_{cm}} \\right) \\text{ dB}$.",
        "automotive_application": "Battery Management System (BMS) Shunt Current Measurement: An EV battery pack carries 400A. A precision $100\\ \\mu\\Omega$ Manganin shunt in the cable drops only $V_{shunt} = 400\\text{ A} \\times 0.0001\\ \\Omega = 40\\text{ mV}$ at full acceleration. An automotive-grade instrumentation amplifier (gain = 100) amplifies this $40\\text{ mV}$ signal to a clean $4.0\\text{ V}$ level for the BMS microcontroller ADC, rejecting 400V DC common-mode bus voltage.",
        "comparison_table": {
            "headers": ["Op-Amp Configuration", "Voltage Gain (Av)", "Input Impedance", "Key Automotive Use Case"],
            "rows": [
                ["Voltage Follower (Buffer)", "Av = 1.0", "Infinite (~10^12 Ω)", "High-impedance sensor isolation (pH, oxygen sensors)"],
                ["Non-Inverting Amplifier", "Av = 1 + (Rf / R1)", "Infinite", "Amplifying unipolar positive sensor voltages (TPS, MAP)"],
                ["Inverting Amplifier", "Av = - (Rf / Rin)", "Finite (Equal to Rin)", "Signal inversion, summing multiple analog sensor channels"],
                ["Instrumentation Amplifier", "Av = [1 + 2R1/Rg] * (R3/R2)", "Ultra-high, balanced", "Wheatstone bridge load cells, strain gauges, battery current shunts"],
                ["Active Low-Pass Filter", "Av(f) = A0 / sqrt(1 + (f/fc)^2)", "High", "Anti-aliasing filter before ADC; removes spark plug EMI"]
            ]
        },
        "formulas": [
            {
                "name": "Non-Inverting Amplifier Gain Formula",
                "math": "V_{out} = V_{in} \\cdot \\left( 1 + \\frac{R_f}{R_1} \\right)",
                "vars": [
                    "V_in = Input analog sensor voltage (Volts)",
                    "R_f = Feedback resistor (Ohms)",
                    "R_1 = Resistor to ground (Ohms)",
                    "V_out = Amplified output voltage (Volts)"
                ],
                "example": "A sensor outputs 0.2V. We want 2.0V output (Gain = 10). If R1 = 10 kΩ, then Rf = (10 - 1) × 10 kΩ = 90 kΩ (Vout = 0.2 × (1 + 90/10) = 2.0 V)."
            },
            {
                "name": "Active Low-Pass Filter Cutoff Frequency",
                "math": "f_c = \\frac{1}{2\\pi \\cdot R \\cdot C}",
                "vars": [
                    "f_c = -3dB Cutoff frequency (Hz)",
                    "R = Filter resistance (Ohms)",
                    "C = Filter capacitance (Farads)"
                ],
                "example": "To filter out 50 Hz alternator ripple from a slow coolant temperature sensor using R = 10 kΩ: C = 1 / (2π × 10000 × 50) = 3.18 × 10^-7 F = 0.318 μF."
            }
        ],
        "code_snippet": """// Python Calculation of Op-Amp Circuit Resistor Values
import numpy as np

def design_non_inverting_amp(target_gain=10.0, r1_ohms=10000.0):
    # Gain = 1 + (Rf / R1) -> Rf = (Gain - 1) * R1
    rf_ohms = (target_gain - 1.0) * r1_ohms
    print(f"Non-Inverting Amp (Gain: {target_gain}x):")
    print(f"  R1 = {r1_ohms/1000:.1f} kΩ,  Rf = {rf_ohms/1000:.1f} kΩ")

def design_lowpass_filter(cutoff_hz=100.0, c_farads=100e-9):
    # fc = 1 / (2 * pi * R * C) -> R = 1 / (2 * pi * fc * C)
    r_ohms = 1.0 / (2.0 * np.pi * cutoff_hz * c_farads)
    print(f"Low-Pass Filter (fc: {cutoff_hz} Hz, C: {c_farads*1e9:.0f} nF):")
    print(f"  Required R = {r_ohms/1000:.2f} kΩ")

design_non_inverting_amp(target_gain=12.5)
design_lowpass_filter(cutoff_hz=50.0)""",
        "must_remember": [
            "Ideal Op-Amp Golden Rules: I+ = I- = 0 (No input current), V+ = V- (Virtual short).",
            "Inverting Gain: Vout = - (Rf / Rin) * Vin.",
            "Non-Inverting Gain: Vout = (1 + Rf / R1) * Vin.",
            "Voltage Follower has Gain = 1, infinite input impedance (zero sensor loading).",
            "Instrumentation amplifiers reject common-mode EMI noise in automotive wire harnesses."
        ],
        "short_qa": [
            ("State the two 'Golden Rules' of ideal operational amplifiers with negative feedback.", "Rule 1: The voltage difference between input terminals is zero ($V_+ = V_-$) due to infinite open-loop gain (Virtual Short). Rule 2: No electrical current flows into either input terminal ($I_+ = I_- = 0$) due to infinite input impedance."),
            ("Why is a voltage follower (buffer) inserted between a high-impedance sensor and an ADC pin?", "High-impedance sensors (such as pH or oxygen sensors) cannot supply significant current without their output voltage sagging (loading error). A voltage follower has near-infinite input impedance (drawing zero current from the sensor) and near-zero output impedance, driving the ADC pin accurately.")
        ],
        "long_qa": [
            ("Derive the closed-loop voltage gain expressions for an Inverting and a Non-Inverting Op-Amp circuit from fundamental Golden Rules. Design a signal conditioning circuit to amplify a 0–100 mV thermocouple signal to 0–5.0 V with a 20 Hz low-pass filter.", "A complete answer covers: (1) Schematics of inverting and non-inverting circuits; (2) Detailed derivations using KCL at summing nodes; (3) Calculation of required gain Av = 5.0V / 0.1V = 50x; (4) Selection of R1 = 10 kΩ, Rf = 490 kΩ; (5) Calculation of RC low-pass filter component values for fc = 20 Hz (R = 10 kΩ, C = 0.8 μF).")
        ],
        "viva_interview_qa": [
            ("What is Common-Mode Rejection Ratio (CMRR) and why is it critical when measuring wheel speed sensor signals in an EV?", "CMRR is the ratio of differential gain to common-mode gain ($CMRR = 20\\log_{10}(A_d / A_{cm})$). In an EV, high-voltage PWM switching from the traction inverter induces large common-mode noise on the wheel speed wiring harness. An amplifier with high CMRR (>90 dB) completely rejects this high-voltage noise while amplifying the small magnetic speed pulses.")
        ],
        "common_mistakes": [
            "Applying the virtual short rule ($V_+ = V_-$) to an open-loop Op-Amp comparator without negative feedback. Virtual short applies ONLY when negative feedback is present.",
            "Forgetting that single-supply automotive Op-Amps (0V to 5V) cannot output negative voltages. Inverting amplifiers require a dual supply or a DC reference bias (e.g., 2.5V virtual ground)."
        ],
        "revision_points": [
            "Golden Rules: I_in = 0, V+ = V-.",
            "Inverting: Vout = -(Rf/Rin)*Vin.",
            "Non-Inverting: Vout = (1 + Rf/R1)*Vin.",
            "Buffer: Gain = 1, Z_in = infinity.",
            "fc = 1 / (2*pi*R*C)."
        ],
        "sources": "Autotronics Lecture 5 Transcript; Electrical & Electronics Fundamentals PPT Slides 118–140; Course Syllabus Section 5."
    }
]

# --- Extra Embedded System Design Topics ---
ESD_EXTRA_TOPICS = [
    {
        "slug": "arm-cortex-m4-nvic-and-exceptions",
        "title": "Nested Vectored Interrupt Controller (NVIC) & Exception Handling",
        "module": "Interrupts & Peripherals",
        "level": "Intermediate",
        "importance": 5,
        "overview": "Real-time automotive microcontrollers must respond instantaneously to asynchronous external events (such as CAN message reception, timer overflows, and ADC conversion completions). The ARM Cortex-M4 integrates the Nested Vectored Interrupt Controller (NVIC) tightly into the core pipeline, providing hardware-managed priority nesting, deterministic 12-cycle interrupt latency, automatic hardware context saving (stacking), Tail-Chaining, and Late-Arrival optimizations.",
        "learning_objectives": [
            "Analyze the ARM Cortex-M4 Exception Model: System Exceptions (Reset, NMI, HardFault, SysTick) vs External Interrupts (IRQs).",
            "Understand the Vector Table structure located at memory address $0\\text{x}00000000$.",
            "Explain NVIC hardware features: Priority grouping (Preemption vs Sub-priority), Tail-Chaining (6-cycle switchover), and Late-Arrival handling.",
            "Trace the automatic hardware stacking and unstacking sequence (R0-R3, R12, LR, PC, xPSR) during interrupt entry and exit."
        ],
        "prerequisites": "ARM Cortex-M4 Core Architecture, Programmer's Model & Registers, Stack Pointer (MSP/PSP).",
        "core_concept": "In older microcontrollers (like 8051 or ARM7), when an interrupt fired, software had to execute dozens of assembly instructions to manually push registers to the stack, identify the interrupt source, and jump to the handler, taking over 50 clock cycles. In the Cortex-M4, the NVIC is built directly inside the CPU silicon: the hardware automatically pushes registers to RAM and branches to the exact ISR address in just **12 clock cycles**.",
        "lecture_notes": "Lecture 4 and 5 of Embedded System Design covered the NVIC in detail. Prof. S. S. Kendre highlighted: 'The NVIC is a vectored interrupt controller. Vectored means the hardware fetches the exact function pointer from the Vector Table in memory; there is zero software polling required!' The professor walked through the 8-register hardware stacking frame (R0-R3, R12, LR, PC, xPSR) and explained how Tail-Chaining saves 18 clock cycles when two interrupts occur back-to-back.",
        "extra_explanation": "Let's analyze the **Cortex-M4 Exception & NVIC Mechanics**:\n\n1. **The Vector Table ($0\\text{x}00000000$ to $0\\text{x}000001FF$):**\n   - Vector 0 ($0\\text{x}00000000$): Initial Main Stack Pointer value (Initial MSP).\n   - Vector 1 ($0\\text{x}00000004$): Initial Program Counter (Reset Handler address with LSB=1).\n   - Vector 2 ($0\\text{x}00000008$): Non-Maskable Interrupt (NMI).\n   - Vector 3 ($0\\text{x}0000000C$): HardFault Handler.\n   - Vector 11 ($0\\text{x}0000002C$): SVCall (Supervisor Call for RTOS).\n   - Vector 14 ($0\\text{x}00000038$): PendSV (Context Switch Handler for RTOS).\n   - Vector 15 ($0\\text{x}0000003C$): SysTick Timer Handler.\n   - Vector 16+ ($0\\text{x}00000040$+): Microcontroller-specific peripheral IRQs (GPIO, Timers, CAN, ADC).\n\n2. **Automatic Hardware Stacking Frame (Interrupt Entry):**\n   - Upon IRQ assertion, the processor hardware automatically pushes **8 registers** onto the current stack in descending order: `xPSR`, `PC` (return address), `LR`, `R12`, `R3`, `R2`, `R1`, `R0`.\n   - The CPU loads the Link Register (LR) with a special **`EXC_RETURN`** value (e.g., $0\\text{xFFFFFFF9}$ to return to Thread mode using MSP, or $0\\text{xFFFFFFFD}$ for Thread mode using PSP).\n   - The CPU loads PC with the ISR address fetched from the Vector Table and begins executing the ISR in Handler Mode in strictly **12 clock cycles**.\n\n3. **NVIC Performance Optimizations:**\n   - **Tail-Chaining:** When an ISR finishes and a second pending interrupt exists, instead of unstacking 8 registers and immediately re-stacking them (24 cycles wasted), the NVIC simply skips unstacking/restacking and branches directly to the next ISR in **only 6 clock cycles**!\n   - **Late-Arrival:** If a higher-priority interrupt arrives while the CPU is in the middle of stacking registers for a lower-priority interrupt, the NVIC dynamically switches to the higher-priority ISR without restarting the stacking process.",
        "workflow_steps": [
            ("Peripheral Event", "CAN controller asserts interrupt line to NVIC"),
            ("Priority Evaluation", "NVIC checks if IRQ priority is higher than currently running task"),
            ("Hardware Context Stacking", "Core automatically pushes R0-R3, R12, LR, PC, xPSR onto stack in 12 cycles"),
            ("Vector Fetch & Mode Switch", "Core fetches ISR address from Vector Table; switches to Handler Mode"),
            ("ISR Execution & EXC_RETURN", "ISR clears interrupt flag; executes BX LR with EXC_RETURN; hardware unstacks frame")
        ],
        "diagram_ascii": """
+-----------------------------------------------------------------------------------+
|               ARM CORTEX-M4 HARDWARE INTERRUPT STACKING FRAME                     |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|    Memory Address (Descending Stack - SP moves down)                              |
|         |                                                                         |
|         |   [ Previous Stack Content (Local variables / Call frames) ]            |
|         |   +--------------------------------------------------------+            |
|         |   |  xPSR       (Program Status Register condition flags)  |  <-- SP + 28|
|         |   +--------------------------------------------------------+            |
|         |   |  PC         (Return Instruction Address to resume)     |  <-- SP + 24|
|         |   +--------------------------------------------------------+            |
|         |   |  LR (R14)   (Subroutine Link Register)                 |  <-- SP + 20|
|         |   +--------------------------------------------------------+            |
|         |   |  R12        (Intra-procedure Scratch Register)         |  <-- SP + 16|
|         |   +--------------------------------------------------------+            |
|         |   |  R3         (Function Parameter / Scratch)             |  <-- SP + 12|
|         |   +--------------------------------------------------------+            |
|         |   |  R2         (Function Parameter / Scratch)             |  <-- SP + 8 |
|         |   +--------------------------------------------------------+            |
|         |   |  R1         (Function Parameter / Scratch)             |  <-- SP + 4 |
|         |   +--------------------------------------------------------+            |
|         v   |  R0         (Function Parameter / Scratch)             |  <-- SP (New)|
|             +--------------------------------------------------------+            |
|                                                                                   |
|    Total Stacking Time: Exactly 12 Clock Cycles (Hardware Autonomous)             |
|                                                                                   |
+-----------------------------------------------------------------------------------+
""",
        "working_principle": "Priority Grouping (Preemption vs Sub-Priority):\nThe NVIC supports up to 256 priority levels (implemented as 16 levels in S32K144 using upper 4 bits of priority registers: $0\\text{x}00$ = highest priority, $0\\text{xF}0$ = lowest priority). Priority can be split into **Preemption Priority** (determines if an interrupt can preempt an actively running ISR) and **Sub-Priority** (determines which interrupt executes first if two arrive simultaneously).",
        "automotive_application": "Anti-Lock Braking System (ABS) Wheel Lock Interrupt: An inductive wheel speed sensor detects an immediate wheel lockup ($0\\text{ RPM}$) during emergency braking. The external pin interrupt asserts IRQ line with highest preemption priority ($0\\text{x}00$). The NVIC preempts the low-priority dashboard display task within $150\\text{ ns}$ (12 cycles at 80 MHz), executing the ABS valve release routine to restore tire traction.",
        "comparison_table": {
            "headers": ["Exception Type", "Exception Number", "Priority Level", "Vector Table Offset", "Core Purpose"],
            "rows": [
                ["Initial MSP", "0", "N/A (Hardware reset value)", "0x00000000", "Top of stack memory address"],
                ["Reset", "1", "-3 (Fixed Highest)", "0x00000004", "First instruction executed on boot"],
                ["NMI (Non-Maskable)", "2", "-2 (Fixed)", "0x00000008", "Critical hardware failure / Watchdog bite"],
                ["HardFault", "3", "-1 (Fixed)", "0x0000000C", "Bus error, unaligned access, illegal opcode"],
                ["SysTick", "15", "Programmable (0 - 15)", "0x0000003C", "1 ms periodic system heartbeat tick for RTOS"],
                ["Peripheral IRQ (0..n)", "16 to 255", "Programmable (0 - 15)", "0x00000040+", "Hardware peripherals (GPIO, CAN, Timers, ADC)"]
            ]
        },
        "formulas": [
            {
                "name": "Interrupt Latency Calculation",
                "math": "T_{latency} = \\frac{12 \\text{ clock cycles}}{f_{clock}}",
                "vars": [
                    "12 = Fixed hardware stacking and vector fetch cycles in ARM Cortex-M4",
                    "f_clock = Microcontroller core operating frequency (Hz)"
                ],
                "example": "On the NXP S32K144 running at f_clock = 80 MHz: T_latency = 12 / (80 × 10^6) = 150 nanoseconds (0.15 μs)."
            }
        ],
        "code_snippet": """// CMSIS NVIC Configuration for S32K144 Peripheral Interrupt
#include "S32K144.h"

void configure_can_interrupt(void) {
    // 1. Set Priority for CAN0 Receive Interrupt (Priority 2, where 0 is highest)
    NVIC_SetPriority(CAN0_ORed_0_15_MB_IRQn, 2);
    
    // 2. Clear any pending CAN0 interrupt flag in NVIC
    NVIC_ClearPendingIRQ(CAN0_ORed_0_15_MB_IRQn);
    
    // 3. Enable the Interrupt in NVIC
    NVIC_EnableIRQ(CAN0_ORed_0_15_MB_IRQn);
}

// Interrupt Service Routine (Vector Table links directly to this function name)
void CAN0_ORed_0_15_MB_IRQHandler(void) {
    // Read received CAN message buffer
    process_rx_can_frame();
    // Clear peripheral interrupt flag in FlexCAN controller
    CAN0->IFLAG1 = (1 << 0);
}""",
        "must_remember": [
            "NVIC provides deterministic 12-cycle interrupt entry latency.",
            "Hardware automatically stacks 8 registers: xPSR, PC, LR, R12, R3, R2, R1, R0.",
            "Tail-Chaining reduces switchover between consecutive interrupts to only 6 clock cycles.",
            "Lower priority number = HIGHER priority (Priority 0 is higher than Priority 5).",
            "Vector Table at 0x00000000 holds Initial MSP (offset 0) and Reset Handler address (offset 4)."
        ],
        "short_qa": [
            ("What eight registers are automatically pushed onto the stack by hardware during ARM Cortex-M4 interrupt entry?", "The 8 registers pushed to the stack (the basic stack frame) are: `xPSR`, `PC` (Program Counter return address), `LR` (Link Register), `R12`, `R3`, `R2`, `R1`, and `R0`."),
            ("What is Tail-Chaining in the ARM Cortex-M4 NVIC?", "Tail-Chaining is an NVIC hardware optimization where, if another interrupt is pending when the current ISR completes, the processor skips unstacking and re-stacking the 8 registers, branching directly to the pending ISR in only 6 clock cycles (saving 18 cycles).")
        ],
        "long_qa": [
            ("Explain the complete ARM Cortex-M4 Exception Model and NVIC operation. Detail the vector table layout, the 12-cycle hardware stacking sequence, priority grouping (preemption vs sub-priority), and the Tail-Chaining and Late-Arrival optimizations.", "A complete answer covers: (1) Vector table diagram from 0x00000000 (Initial MSP, Reset, NMI, HardFault, SysTick, IRQs); (2) Step-by-step 12-cycle hardware stacking diagram showing all 8 registers; (3) EXC_RETURN magic codes; (4) Preemption vs Sub-priority grouping bits; (5) Tail-Chaining (6-cycle transition) and Late-Arrival diagrams.")
        ],
        "viva_interview_qa": [
            ("What is the purpose of the special `EXC_RETURN` value loaded into the Link Register (LR) when an ISR begins execution?", "In Cortex-M, LR is not loaded with the return address during an interrupt. Instead, it is loaded with a special `EXC_RETURN` bit-pattern (e.g., $0\\text{xFFFFFFF9}$ or $0\\text{xFFFFFFFD}$). When the ISR executes `BX LR` at completion, the hardware detects the `0xFFFFFFF` prefix, triggers the automatic hardware unstacking of registers from memory, and restores processor mode (Thread/Handler) and active stack pointer (MSP/PSP).")
        ],
        "common_mistakes": [
            "Assuming higher priority numbers mean higher priority. In ARM Cortex-M, **lower numerical values represent higher priority** ($0 = \\text{Highest}, 15 = \\text{Lowest}$).",
            "Forgetting to clear the peripheral's interrupt flag inside the ISR. If the peripheral flag is not cleared, the NVIC will re-trigger the exact same ISR indefinitely in an infinite lockup loop."
        ],
        "revision_points": [
            "NVIC = 12-cycle deterministic latency.",
            "Hardware pushes: xPSR, PC, LR, R12, R3, R2, R1, R0.",
            "Tail-Chaining = 6-cycle transition without restacking.",
            "Lower priority number = HIGHER priority (0 > 15).",
            "EXC_RETURN triggers automatic hardware unstacking."
        ],
        "sources": "Embedded System Design Lecture 4 & 5 Transcripts; The Definitive Guide to ARM Cortex-M3/M4 Processors Chapter 7; Course Syllabus Section 4."
    },
    {
        "slug": "s32k144-gpio-configuration-and-driver",
        "title": "NXP S32K144 GPIO Architecture & Low-Level Driver Development",
        "module": "Microcontroller Peripherals",
        "level": "Intermediate",
        "importance": 5,
        "overview": "General Purpose Input/Output (GPIO) ports provide the primary digital interface between the NXP S32K144 automotive microcontroller and external hardware circuits (switches, LEDs, relays, and transceivers). S32K144 GPIO configuration requires a 3-tier hardware register hierarchy: Peripheral Clock Control (PCC), Port Control Register (PORT_PCR for multiplexing, pull-up/down, and pin interrupts), and GPIO Data Direction / Output Registers (PDDR, PDOR, PSOR, PCOR, PTOR, and PDIR).",
        "learning_objectives": [
            "Deconstruct the 3-step S32K144 GPIO initialization workflow: Clock Gating, Pin Muxing, and Data Direction.",
            "Configure Peripheral Clock Control (PCC) registers to enable clock trees to Port modules.",
            "Configure Pin Control Registers (PORT_PCRn) for GPIO multiplexing (MUX=001), internal pull-up/pull-down, and passive filtering.",
            "Write bare-metal register-level embedded C drivers to read digital inputs and toggle outputs using atomic bit-set and bit-clear registers."
        ],
        "prerequisites": "ARM Cortex-M4 Core, Embedded C, Memory-Mapped I/O, Bitwise Operations (`|`, `&`, `^`, `~`).",
        "core_concept": "To maximize energy efficiency, all peripherals in the S32K144 are powered down with their clocks turned off upon reset. You cannot simply write to a GPIO pin! You must first: (1) Turn ON the clock gate in the PCC module, (2) Configure the pin multiplexer in the PORT module so the physical package pin connects to the internal GPIO hardware block, and (3) Set pin direction (Input or Output) in the GPIO module.",
        "lecture_notes": "Lecture 2, 4, and 6 of Embedded System Design and Lab Session 1 detailed S32K144 GPIO programming. Prof. S. S. Kendre and Prof. Shree Prasad M. emphasized: 'The S32K144 has 5 GPIO ports: PTA, PTB, PTC, PTD, and PTE. Each pin has a dedicated PORT_PCR register. If you forget to enable the clock in PCC_PORTx or forget to set MUX = 0b001, your GPIO code will fail silently!' The instructors walked through atomic bit manipulation using PSOR (Set) and PCOR (Clear) registers.",
        "extra_explanation": "Let's analyze the **3-Tier S32K144 GPIO Register Hierarchy**:\n\n1. **Tier 1: Peripheral Clock Control (PCC):**\n   - Enables the clock signal to the Port hardware module.\n   - Register: `PCC->PCCn[PCC_PORTD_INDEX] |= PCC_PCCn_CGC_MASK;` (Sets Clock Gating Control bit).\n\n2. **Tier 2: Port Control Register (PORT_PCRn):**\n   - Configures the electrical characteristics and pin routing of individual pin $n$ ($0$ to $31$).\n   - **MUX Bits (Bits 10-8):** `000` = Analog, `001` = GPIO, `010-111` = Alternate peripheral functions (UART, SPI, CAN, PWM).\n   - **PE (Bit 1):** Pull Enable ($1 = \\text{Active}$, $0 = \\text{Disabled}$).\n   - **PS (Bit 0):** Pull Select ($1 = \\text{Pull-Up}$, $0 = \\text{Pull-Down}$).\n   - **IRQC (Bits 19-16):** Interrupt Configuration (Rising edge, falling edge, both edges, or logic low).\n\n3. **Tier 3: GPIO Direction & Data Registers (GPIO_Type):**\n   - **PDDR (Port Data Direction):** Bit $n = 1$ configures Pin $n$ as **Output**; Bit $n = 0$ configures Pin $n$ as **Input**.\n   - **PDOR (Port Data Output):** Read/write full 32-bit output latch.\n   - **PSOR (Port Set Output):** Writing 1 atomically drives pin HIGH (writing 0 has no effect).\n   - **PCOR (Port Clear Output):** Writing 1 atomically drives pin LOW (writing 0 has no effect).\n   - **PTOR (Port Toggle Output):** Writing 1 atomically inverts the pin state.\n   - **PDIR (Port Data Input):** Read-only register reflecting the physical logic level (1 or 0) on the external pin.",
        "workflow_steps": [
            ("Step 1: Enable Clock (PCC)", "PCC->PCCn[PCC_PORTD_INDEX] |= PCC_PCCn_CGC_MASK"),
            ("Step 2: Pin MUX & Pull (PORT_PCR)", "PORTD->PCR[15] = PORT_PCR_MUX(1) | PORT_PCR_PE_MASK | PORT_PCR_PS_MASK"),
            ("Step 3: Set Direction (GPIO_PDDR)", "PTD->PDDR |= (1 << 15) for Output; PTD->PDDR &= ~(1 << 15) for Input"),
            ("Step 4: Output Write / Atomic Control", "PTD->PSOR = (1 << 15) to set High; PTD->PCOR = (1 << 15) to set Low"),
            ("Step 5: Input Read", "uint32_t state = (PTD->PDIR >> 15) & 0x01")
        ],
        "diagram_ascii": """
+-----------------------------------------------------------------------------------+
|               NXP S32K144 3-TIER GPIO ARCHITECTURE & DATA FLOW                    |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|    1. CLOCK GATING (PCC)                                                          |
|       [ System Clock 80 MHz ] ---> [ PCC_PORTx (CGC Bit = 1) ] ---> Clock Enabled|
|                                                                                   |
|    2. PIN MULTIPLEXING (PORT_PCRn)                                                |
|       +------------------------------------------------------------------------+  |
|       | PORTx_PCRn Register                                                    |  |
|       | [ IRQC (19:16) Interrupt ] [ MUX (10:8) = 001 GPIO ] [ PE Pull ] [ PS ]|  |
|       +------------------------------------------------------------------------+  |
|                                         |                                         |
|    3. GPIO HARDWARE CORE                v                                         |
|       +------------------------------------------------------------------------+  |
|       | GPIOx Module                                                           |  |
|       |                                                                        |  |
|       |  Direction:  PDDR Register (Bit n: 1 = Output, 0 = Input)              |  |
|       |                                                                        |  |
|       |  Outputs:    PSOR (Atomic Set)   PCOR (Atomic Clear)   PTOR (Toggle)   |  |
|       |              -----------------   -------------------   -------------   |  |
|       |                      \                   /                             |  |
|       |                       v                 v                              |  |
|       |                      [ PDOR Data Output Latch ]                        |  |
|       |                                 |                                      |  |
|       |  Input:              [ PDIR Data Input Buffer ] <==== [ Physical Pin ] |  |
|       +------------------------------------------------------------------------+  |
|                                                                                   |
+-----------------------------------------------------------------------------------+
""",
        "working_principle": "Why Atomic Bit Registers (PSOR / PCOR) are Essential:\nIn multi-tasking and interrupt-driven embedded systems, modifying a shared output register using standard read-modify-write syntax (`PDOR |= (1 << 15);`) is a major race condition bug: if an interrupt occurs midway through the 3-cycle load-or-store instruction sequence, other pin states are corrupted. **PSOR and PCOR** allow writing a `1` directly to the target bit in a single atomic bus transaction with zero impact on other pins and zero race conditions.",
        "automotive_application": "Brake Pedal Switch Input & Brake Lamp Output: The brake pedal switch is connected to Port C Pin 12 with an internal pull-up resistor. When the driver presses the brake pedal, PTC12 is pulled to ground (logic 0). The S32K144 GPIO interrupt reads PDIR, verifies pedal press, and immediately drives Port D Pin 15 (Brake Light Relay) HIGH using `PTD->PSOR = (1 << 15);` within 10 microseconds.",
        "comparison_table": {
            "headers": ["Register Name", "Full Description", "Access Mode", "Primary Function"],
            "rows": [
                ["PCC_PORTx", "Peripheral Clock Control", "Read / Write", "Enables clock gate (CGC bit) to Port module"],
                ["PORTx_PCRn", "Port Pin Control Register n", "Read / Write", "Pin multiplexer (MUX), pull-up/down, slew rate, interrupt mode"],
                ["GPIOx_PDDR", "Port Data Direction Register", "Read / Write", "Configures individual pin as Input (0) or Output (1)"],
                ["GPIOx_PSOR", "Port Set Output Register", "Write Only", "Writing 1 atomically drives pin HIGH (3.3V / 5.0V)"],
                ["GPIOx_PCOR", "Port Clear Output Register", "Write Only", "Writing 1 atomically drives pin LOW (0.0V Ground)"],
                ["GPIOx_PTOR", "Port Toggle Output Register", "Write Only", "Writing 1 atomically inverts current output state"],
                ["GPIOx_PDIR", "Port Data Input Register", "Read Only", "Reads raw digital logic level present on physical external pin"]
            ]
        },
        "formulas": [
            {
                "name": "GPIO Atomic Bit Mask Calculation",
                "math": "\\text{Mask} = (1 \\ll \\text{Pin Number}), \\quad \\text{Set: } \\text{PSOR} = \\text{Mask}, \\quad \\text{Clear: } \\text{PCOR} = \\text{Mask}",
                "vars": [
                    "Pin Number = Target pin (0 to 31) on Port A, B, C, D, or E",
                    "1 << n = Binary bitmask shifting bit 1 to position n"
                ],
                "example": "To toggle RGB Blue LED on Port D Pin 0 (PTD0): Mask = (1 << 0) = 0x00000001. PTD->PTOR = 0x00000001."
            }
        ],
        "code_snippet": """// S32K144 Complete Bare-Metal GPIO Driver Example (RGB LED Control)
#include "S32K144.h"

#define RED_LED_PIN    15  // PTD15
#define BLUE_LED_PIN   0   // PTD0
#define BUTTON_PIN     12  // PTC12 (Input with Pull-Up)

void gpio_init(void) {
    // 1. Enable Clocks to PORTC and PORTD
    PCC->PCCn[PCC_PORTC_INDEX] |= PCC_PCCn_CGC_MASK;
    PCC->PCCn[PCC_PORTD_INDEX] |= PCC_PCCn_CGC_MASK;
    
    // 2. Configure PTD15 and PTD0 as GPIO Outputs
    PORTD->PCR[RED_LED_PIN] = PORT_PCR_MUX(1);
    PORTD->PCR[BLUE_LED_PIN] = PORT_PCR_MUX(1);
    PTD->PDDR |= (1 << RED_LED_PIN) | (1 << BLUE_LED_PIN);
    
    // 3. Configure PTC12 as GPIO Input with Internal Pull-Up Resistor
    PORTC->PCR[BUTTON_PIN] = PORT_PCR_MUX(1) | PORT_PCR_PE_MASK | PORT_PCR_PS_MASK;
    PTC->PDDR &= ~(1 << BUTTON_PIN); // Input direction
}

int main(void) {
    gpio_init();
    while (1) {
        // Read button state (Active Low: 0 when pressed)
        if ((PTC->PDIR & (1 << BUTTON_PIN)) == 0) {
            PTD->PSOR = (1 << RED_LED_PIN);  // Turn ON Red LED
            PTD->PCOR = (1 << BLUE_LED_PIN); // Turn OFF Blue LED
        } else {
            PTD->PCOR = (1 << RED_LED_PIN);  // Turn OFF Red LED
            PTD->PSOR = (1 << BLUE_LED_PIN); // Turn ON Blue LED
        }
    }
}""",
        "must_remember": [
            "3-step GPIO initialization: (1) Clock in PCC, (2) Pin MUX in PORT_PCR, (3) Direction in PDDR.",
            "MUX = 0b001 (MUX=1) selects GPIO mode in PORT_PCRn.",
            "Use PSOR (Set) and PCOR (Clear) for atomic thread-safe pin manipulation.",
            "PDIR is read-only for digital inputs; PDDR configures direction (1=Output, 0=Input)."
        ],
        "short_qa": [
            ("What are the three essential register configuration steps required to initialize a GPIO output pin on the NXP S32K144?", "Step 1: Enable the peripheral clock for the corresponding Port in the Peripheral Clock Control (PCC) register (set CGC bit). Step 2: Configure the pin multiplexer in `PORTx_PCRn` to GPIO mode (`MUX = 001`). Step 3: Set the pin direction bit to Output (`1`) in the Port Data Direction Register (`GPIOx_PDDR`)."),
            ("Why should an embedded developer use the PSOR and PCOR registers instead of writing directly to PDOR?", "Modifying `PDOR` directly (`PDOR |= (1 << pin)`) requires a multi-cycle Read-Modify-Write operation that is prone to race conditions if an interrupt occurs mid-execution. `PSOR` (Set) and `PCOR` (Clear) perform single-cycle atomic write operations that modify only the targeted pin without affecting other pins on the port.")
        ],
        "long_qa": [
            ("Explain the complete 3-tier GPIO architecture of the NXP S32K144 microcontroller. Detail the roles of PCC, PORT, and GPIO register blocks. Write a complete bare-metal C program to configure Port D Pin 15 as an output LED and Port C Pin 12 as an input push-button with an internal pull-up resistor.", "A complete answer covers: (1) 3-tier register block diagram (PCC -> PORT_PCR -> GPIO); (2) Explanation of PCC clock gating, PORT_PCR multiplexing/pull-up/interrupt bits, and GPIO direction/data registers; (3) Explanation of atomic PSOR/PCOR/PTOR registers; (4) Fully commented bare-metal C code demonstrating clock initialization, pin muxing, pull-up configuration, and polling loop.")
        ],
        "viva_interview_qa": [
            ("What happens if you attempt to write to `PORTD->PCR[15]` before enabling `PCC_PCCn_CGC_MASK` in the PCC register?", "Because the clock tree to PORTD is gated off (unpowered), the bus matrix cannot communicate with the PORTD peripheral address space. The CPU core encounters a bus access timeout and immediately triggers an unrecoverable **BusFault / HardFault** exception.")
        ],
        "common_mistakes": [
            "Writing to `PORT_PCR` or `GPIO_PDDR` without first enabling the clock in `PCC`. This causes an immediate HardFault exception.",
            "Setting `PTD->PDDR = (1 << 15)` instead of `PTD->PDDR |= (1 << 15)`. Using `=` overwrites all other 31 pin directions on that port to inputs!"
        ],
        "revision_points": [
            "1. PCC: Enable Clock (CGC=1).",
            "2. PORT_PCR: Set MUX=1 (GPIO) + Pull-up/down.",
            "3. GPIO_PDDR: 1=Output, 0=Input.",
            "4. Control: PSOR (Set), PCOR (Clear), PTOR (Toggle), PDIR (Read)."
        ],
        "sources": "Embedded System Design Lecture 2 & 4 Transcripts; S32K144 Reference Manual Chapter 11 (PORT) & Chapter 12 (GPIO); Lab 1 Manual."
    }
]

def append_topics_to_file(filepath, new_topics):
    content = filepath.read_text(encoding='utf-8')
    # Find the end of TOPICS list
    idx = content.rfind(']')
    if idx == -1:
        print(f"Error: Could not find closing bracket in {filepath}")
        return
    
    # Format new topics
    import pprint
    topics_str = ""
    for t in new_topics:
        topics_str += ",\n" + pprint.pformat(t, width=100, sort_dicts=False)
    
    new_content = content[:idx] + topics_str + "\n]" + content[idx+1:]
    filepath.write_text(new_content, encoding='utf-8')
    print(f"Appended {len(new_topics)} topics to {filepath.name}")

if __name__ == '__main__':
    append_topics_to_file(TOOLS_DIR / "data_av.py", AV_EXTRA_TOPICS)
    append_topics_to_file(TOOLS_DIR / "data_at.py", AT_EXTRA_TOPICS)
    append_topics_to_file(TOOLS_DIR / "data_esd.py", ESD_EXTRA_TOPICS)
