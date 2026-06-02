# AI Office Hours — Copilot Demo

GitHub Copilot demo using dehumidifier lab data. Three self-contained demos, ~15-20 min total.

---

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Open the project folder in VS Code:
   ```bash
   code .
   ```
3. Confirm GitHub Copilot is active (icon in the VS Code status bar, bottom right).

---

## Demo 1 — Find the Fault (~5 min)

**Open:** `demo_1_find_faults.py`

**Say:** *"I've got a CSV with readings from 6 dehumidifier units. Let me ask Copilot to find any problems."*

**Type this comment** (it's already there — just position your cursor at the end of line 3 and press Enter):
```
# Load test_run_data.csv and print a summary of any FAULT rows, including which unit and when
```

**Wait for Copilot** to suggest code (grey text appears). Press **Tab** to accept.

**Run it:**
```bash
python demo_1_find_faults.py
```

**Expected output:**
```
Found 1 fault(s):

  Unit        Timestamp  TempF  RH_pct Status
DH-004 2026-06-01 09:30   74.8      63  FAULT
```

**Say:** *"DH-004 had a fault at 9:30 AM — temperature 74.8°F, humidity 63%. Copilot wrote all of that from one comment."*

**If Copilot doesn't cooperate:** Open `solutions/demo_1_complete.py` and run that instead.

---

## Demo 2 — Visualize Humidity Trends (~7 min)

**Open:** `demo_2_humidity_chart.py`

**Say:** *"Now let's visualize humidity across all units over time."*

**Position cursor** at the end of line 4 (the comment) and press Enter.

**Wait for Copilot** to suggest code. Press **Tab** to accept. It may suggest line by line — keep pressing Tab.

**Run it:**
```bash
python demo_2_humidity_chart.py
```

**Expected output:** A chart window opens with 6 colored lines, one per unit. A dashed grey line marks the 50% setpoint.

**Say:** *"Each line is a different unit. You can immediately see which units are trending high and which dipped below the comfort band. This would have taken 20 minutes to write from scratch — Copilot did it in seconds."*

**If Copilot doesn't cooperate:** Open `solutions/demo_2_complete.py` and run that instead.

---

## Demo 3 — Diagnose from the Log (~5 min)

**Open:** `demo_3_log_summary.py`

**Say:** *"Last one — raw log files. Same idea, different format."*

**Position cursor** at the end of line 1 and press Enter.

**Wait for Copilot** to suggest code. No imports were given — watch what it picks.

**Run it:**
```bash
python demo_3_log_summary.py
```

**Expected output:**
```
Found 3 issue(s) in log:

[2026-06-01 10:36] WARN  RH 43% below comfort band (45-55)
[2026-06-01 11:02] ERROR E04 RH sensor read timeout, retry 1 of 3
[2026-06-01 11:02] ERROR E04 RH sensor read timeout, retry 2 of 3
```

**Say:** *"There's a sensor that timed out twice in a row. Without this script, you'd be scrolling through the log manually. Copilot extracted every issue in one comment."*

**If Copilot doesn't cooperate:** Open `solutions/demo_3_complete.py` and run that instead.

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Copilot suggests wrong code | Press Escape, rephrase the comment slightly, wait again |
| Copilot shows no suggestion | Check the Copilot icon in the status bar — it should be spinning. Try Alt+\ to trigger manually. |
| Script errors on run | Open the matching `solutions/` file and run that instead — pivot smoothly: *"Let me show you the finished version"* |
| Chart doesn't open | Run `pip install matplotlib` and try again |
