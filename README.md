# M.Tech Automotive Engineering Study Guide & Exam Knowledge Base

A professional, responsive, and exam-oriented **M.Tech Automotive Engineering Study Guide Website** built from official BITS Pilani Semester 1 lecture transcripts, slides, handouts, and laboratory sessions.

---

## 🌟 Key Features

1. **4 Core Semester 1 Subjects:**
   - **Automotive Communication Systems (`AELZG513`)**: V2X (DSRC, C-V2X), Physical Channel Modeling, In-Vehicle Networks (CAN 2.0B, CAN-FD, LIN, FlexRay, Automotive Ethernet), and Vector DBC/TS Master Lab Workflows.
   - **Automotive Vehicle (`AELZC441`)**: Homologation (UN ECE/AIS), Tractive Effort & Road Loads, Powertrain Architectures (FF, FR, Dual-Motor EV), 4-Stroke Otto/Diesel Cycles, Engine Performance & BSFC, Modern Transmissions (MT, AT, DCT, CVT, Planetary), EV Powertrains (PMSM, Inverters, Battery NMC/LFP), Suspension, Steering, and Braking.
   - **Autotronics (`AEZG533 / AELZG533`)**: Systems & Signal Flow, Voltage Dividers, RLC Physics, Circuit Theorems (KCL, KVL, Thévenin Equivalent, Max Power Transfer), BJT & Power MOSFET Switching, Op-Amps & Instrumentation Amplifiers, Data Converters (12-bit SAR ADC, DAC), and Engine Sensors.
   - **Embedded System Design (`AEZG512 / AELZC512`)**: Embedded Systems Foundations, Microprocessor vs Microcontroller, ARM Cortex-M4 32-bit RISC Architecture, Programmer's Model (MSP/PSP, Thread/Handler Modes, xPSR), NVIC Exception Model (12-cycle latency, Hardware Stacking, Tail-Chaining), NXP S32K144 MCU, 3-Tier GPIO Drivers, Timers, PWM, ADC, and FlexCAN Controller.

2. **20-Section Standardized Topic Page Architecture:**
   - Breadcrumbs & Course Metadata (Difficulty, Exam Importance, Course Code)
   - Action Bar (Study Status, Bookmark, Print / PDF)
   - Quick Overview
   - Learning Objectives & Prerequisites
   - Core Concept & Physical Intuition (Tailored from Backbencher to Topper)
   - In-Class Lecture Transcript Synthesis (`📘 Lecture Notes`)
   - Rigorous Engineering Theory & Mathematical Derivations (`💡 Additional Explanation`)
   - Step-by-Step Architecture & Signal Workflow
   - ASCII / System Architecture Diagrams
   - Step-by-Step Working Principles
   - Real Automotive Application & Industry Case Studies
   - Technical Comparison & Specifications Table
   - Important Mathematical Formulas with Variable Definitions & Worked Numericals
   - Embedded C / Register Configuration Driver Code Blocks with Copy Feature
   - Must-Remember Key Points for Examinations
   - Common Student Misconceptions & Exam Traps (`⚠️ Warning Boxes`)
   - Exam Preparation & Model Questions:
     - Short Answer Questions (1–2 Marks)
     - Comprehensive Long Answer Questions (5–10 Marks)
     - Viva Voce & Technical Interview Questions
   - 60-Second Flash / Revision Card
   - Personal Local Notes (auto-saved to browser `localStorage`)
   - Source Traceability & Previous/Next Navigation

3. **Client-Side Interactive Core:**
   - **Instant Search:** Press `Ctrl+K` or `/` to search across all topics, formulas, registers, and exam questions offline.
   - **Study Tracking:** Mark topics as `☐ Not Started`, `◐ Studying`, or `☑ Mastered`.
   - **Theme Switching:** Sleek Academic Dark Mode & Clean Modern Light Mode.
   - **Private & Offline:** Works 100% offline directly from disk without any database or internet requirement.

---

## 🚀 How to Run the Website Locally

### Option 1: Using Built-in Python Web Server (Recommended)
From the project root directory, run:
```bash
python -m http.server 8000 --directory StudyGuide
```
Then open your web browser and navigate to:
```text
http://localhost:8000
```

### Option 2: Direct File Access (Zero Server Required)
Simply double-click:
```text
C:\Users\admin\OneDrive\Documents\Mtech_AE_Notes\StudyGuide\index.html
```

---

## 🛠️ Rebuilding & Validating the Site

The master build script automatically processes raw lecture notes, extracts transcript text, builds search indices, generates all HTML pages, and runs integrity checks.

```bash
# Run the complete build and verification pipeline
python build.py

# Run standalone integrity verification
python validate.py
```

---

## 📁 Repository Structure

```text
Mtech_AE_Notes/
├── Automotive Communication/     # [Read-Only] Raw DOCX transcripts, PDFs, Slides
├── Automotive Vehicle/           # [Read-Only] Raw DOCX transcripts, PDFs, Slides
├── Autotronics/                  # [Read-Only] Raw DOCX transcripts, PDFs, Slides
├── Embedded System Design/       # [Read-Only] Raw DOCX transcripts, PDFs, Slides
├── StudyGuide/                   # Generated Static Website
│   ├── index.html                # Master Portal Homepage
│   ├── semesters/
│   │   └── sem1.html             # Semester 1 Hub
│   ├── subjects/                 # 4 Subject Dashboards
│   │   ├── automotive-communication.html
│   │   ├── automotive-vehicle.html
│   │   ├── autotronics.html
│   │   └── embedded-system-design.html
│   ├── topics/                   # Individual Detailed Topic Pages
│   │   ├── automotive-communication/
│   │   ├── automotive-vehicle/
│   │   ├── autotronics/
│   │   └── embedded-system-design/
│   ├── css/
│   │   └── style.css             # Unified CSS Design System (Light/Dark themes)
│   ├── js/
│   │   ├── app.js                # Search, Theme, Progress, Notes, Bookmarks
│   │   └── search-index.js       # Offline search data
│   └── data/
│       ├── search-index.json     # Searchable topic index
│       ├── topics.json           # All topics metadata
│       ├── subjects.json         # Subjects metadata
│       └── source-inventory.json # Scanned lecture files & word counts
├── tools/
│   ├── topic_data.py             # Master topic aggregator
│   ├── data_ac.py                # Automotive Communication dataset
│   ├── data_av.py                # Automotive Vehicle dataset
│   ├── data_at.py                # Autotronics dataset
│   ├── data_esd.py               # Embedded System Design dataset
│   ├── scan_notes.py             # Raw transcript scanner
│   ├── build_search_index.py     # Search index generator
│   └── generate_html.py          # HTML page generator
├── build.py                      # Master build pipeline
├── validate.py                   # Integrity validator
└── README.md                     # Documentation
```

---
*Built for M.Tech Automotive Engineering students at BITS Pilani (Work Integrated Learning Programmes).*
