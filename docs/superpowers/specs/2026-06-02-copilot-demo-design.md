# AI Office Hours — Copilot Demo Design

**Date:** 2026-06-02  
**Audience:** Mixed (technical and non-technical)  
**Duration:** 15–20 minutes  
**Format:** Live coding with GitHub Copilot

---

## Goal

Demonstrate GitHub Copilot's ability to write useful data analysis code from plain-English comments, using real-looking lab data from dehumidifier test runs. Each demo is self-contained so the presenter can recover easily if something goes wrong.

---

## Data Files

| File | Description |
|------|-------------|
| `data/test_run_data.csv` | 6 dehumidifier units (DH-001 to DH-006), readings every 15 min: timestamp, temp (°F), humidity (%), status. DH-004 has a FAULT event. |
| `data/dehumidifier_serial.log` | Raw serial output from one unit: boot info, compressor on/off cycles, an E04 RH sensor timeout error, and a humidity comfort band warning. |

---

## Project Structure

```
ai-office-hours-demo/
├── data/
│   ├── test_run_data.csv
│   └── dehumidifier_serial.log
├── demo_1_find_faults.py       # starter: imports + comment prompt only
├── demo_2_humidity_chart.py    # starter: imports + comment prompt only
├── demo_3_log_summary.py       # starter: imports + comment prompt only
├── solutions/
│   ├── demo_1_complete.py      # safety net if Copilot misbehaves
│   ├── demo_2_complete.py
│   └── demo_3_complete.py
├── requirements.txt
└── README.md                   # speaker notes with step-by-step demo script
```

---

## Demos

### Demo 1 — Find the Fault (~5 min)

**File:** `demo_1_find_faults.py`  
**Starter contents:** `import pandas as pd` + one plain-English comment  
**Copilot writes:** pandas code to load the CSV and print a summary of FAULT rows  
**Expected output:** Table showing DH-004 had a FAULT at 2026-06-01 09:30, temp 74.8°F, RH 63%  
**Audience takeaway:** Copilot can translate "find the problem rows" into working code instantly

### Demo 2 — Visualize Humidity Trends (~7 min)

**File:** `demo_2_humidity_chart.py`  
**Starter contents:** `import pandas as pd` + `import matplotlib.pyplot as plt` + one comment  
**Copilot writes:** multi-line chart, one colored line per unit, labeled axes  
**Expected output:** Line chart showing all 6 units' humidity over time (DH-006 spike visible)  
**Audience takeaway:** From a comment to a chart in seconds — no Stack Overflow needed

### Demo 3 — Diagnose from the Log (~5 min)

**File:** `demo_3_log_summary.py`  
**Starter contents:** One comment prompt (no imports — let Copilot choose)  
**Copilot writes:** File-reading code that filters and prints ERROR/WARN lines with timestamps  
**Expected output:** E04 sensor timeout errors and the RH comfort band warning, cleanly formatted  
**Audience takeaway:** Same technique works on raw log files, not just structured data

---

## Safety Net

Each `solutions/demo_N_complete.py` contains a working, tested version of that demo. If Copilot produces incorrect or unhelpful output during the live session, the presenter can open the solution file and run it instead without breaking the narrative.

---

## Dependencies

- `pandas` — CSV loading and filtering
- `matplotlib` — chart generation

No other dependencies. Both are standard data science packages installable with `pip install pandas matplotlib`.

---

## README / Speaker Notes

The README will include:
- Setup instructions (copy data files, `pip install -r requirements.txt`)
- Step-by-step script for each demo: what comment to type, what output to expect, what to say to the audience
- Troubleshooting tips (what to do if Copilot suggests wrong code)
