# Copilot Demo Project Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a ready-to-run demo project that lets a presenter live-code with GitHub Copilot against real dehumidifier lab data for a 15-20 min mixed-audience office hours session.

**Architecture:** Three self-contained starter scripts (imports + comment only) pair with three complete solution scripts (working code) as safety nets. Data files are copied into the repo. A README serves as speaker notes.

**Tech Stack:** Python, pandas, matplotlib

---

## File Map

| File | Role |
|------|------|
| `data/test_run_data.csv` | Copied from ~/Downloads |
| `data/dehumidifier_serial.log` | Copied from ~/Downloads |
| `demo_1_find_faults.py` | Starter: imports + comment prompt only |
| `demo_2_humidity_chart.py` | Starter: imports + comment prompt only |
| `demo_3_log_summary.py` | Starter: comment prompt only (no imports) |
| `solutions/demo_1_complete.py` | Working fault-finder using pandas |
| `solutions/demo_2_complete.py` | Working humidity chart using matplotlib |
| `solutions/demo_3_complete.py` | Working log parser using plain file I/O |
| `requirements.txt` | pandas, matplotlib |
| `README.md` | Setup + step-by-step speaker notes |

---

### Task 1: Project setup — data files and requirements

**Files:**
- Create: `data/test_run_data.csv` (copy from ~/Downloads)
- Create: `data/dehumidifier_serial.log` (copy from ~/Downloads)
- Create: `requirements.txt`
- Create: `solutions/` directory

- [ ] **Step 1: Copy data files into the repo**

```bash
cp ~/Downloads/test_run_data.csv /Users/kalynnwillis/ai-office-hours-demo/data/
cp ~/Downloads/dehumidifier_serial.log /Users/kalynnwillis/ai-office-hours-demo/data/
mkdir -p /Users/kalynnwillis/ai-office-hours-demo/solutions
```

- [ ] **Step 2: Verify files are present and non-empty**

```bash
ls -lh /Users/kalynnwillis/ai-office-hours-demo/data/
```

Expected: Both files listed with non-zero sizes.

- [ ] **Step 3: Write requirements.txt**

Create `/Users/kalynnwillis/ai-office-hours-demo/requirements.txt`:

```
pandas
matplotlib
```

- [ ] **Step 4: Commit**

```bash
cd /Users/kalynnwillis/ai-office-hours-demo
git add data/ solutions/ requirements.txt
git commit -m "Add data files and requirements"
```

---

### Task 2: Starter script — Demo 1 (find faults)

**Files:**
- Create: `demo_1_find_faults.py`

- [ ] **Step 1: Write the starter file**

Create `/Users/kalynnwillis/ai-office-hours-demo/demo_1_find_faults.py`:

```python
import pandas as pd

# Load test_run_data.csv and print a summary of any FAULT rows, including which unit and when
```

- [ ] **Step 2: Verify the file is exactly 3 lines**

```bash
cat /Users/kalynnwillis/ai-office-hours-demo/demo_1_find_faults.py
```

Expected: import line, blank line, comment line. No actual logic — that's for Copilot.

- [ ] **Step 3: Commit**

```bash
cd /Users/kalynnwillis/ai-office-hours-demo
git add demo_1_find_faults.py
git commit -m "Add starter script for Demo 1 (find faults)"
```

---

### Task 3: Solution script — Demo 1 (find faults)

**Files:**
- Create: `solutions/demo_1_complete.py`

- [ ] **Step 1: Write the complete solution**

Create `/Users/kalynnwillis/ai-office-hours-demo/solutions/demo_1_complete.py`:

```python
import pandas as pd

# Load test_run_data.csv and print a summary of any FAULT rows, including which unit and when

df = pd.read_csv('data/test_run_data.csv')
faults = df[df['Status'] == 'FAULT']

if faults.empty:
    print("No faults found.")
else:
    print(f"Found {len(faults)} fault(s):\n")
    print(faults[['Unit', 'Timestamp', 'TempF', 'RH_pct', 'Status']].to_string(index=False))
```

- [ ] **Step 2: Run the solution and verify output**

```bash
cd /Users/kalynnwillis/ai-office-hours-demo
python solutions/demo_1_complete.py
```

Expected output:
```
Found 1 fault(s):

  Unit            Timestamp  TempF  RH_pct Status
DH-004  2026-06-01 09:30   74.8      63  FAULT
```

- [ ] **Step 3: Commit**

```bash
git add solutions/demo_1_complete.py
git commit -m "Add solution script for Demo 1"
```

---

### Task 4: Starter script — Demo 2 (humidity chart)

**Files:**
- Create: `demo_2_humidity_chart.py`

- [ ] **Step 1: Write the starter file**

Create `/Users/kalynnwillis/ai-office-hours-demo/demo_2_humidity_chart.py`:

```python
import pandas as pd
import matplotlib.pyplot as plt

# Plot humidity (RH_pct) over time for each unit as a separate colored line, with a legend and labeled axes
```

- [ ] **Step 2: Verify the file contains only imports and the comment**

```bash
cat /Users/kalynnwillis/ai-office-hours-demo/demo_2_humidity_chart.py
```

Expected: two import lines, blank line, comment. No logic.

- [ ] **Step 3: Commit**

```bash
git add demo_2_humidity_chart.py
git commit -m "Add starter script for Demo 2 (humidity chart)"
```

---

### Task 5: Solution script — Demo 2 (humidity chart)

**Files:**
- Create: `solutions/demo_2_complete.py`

- [ ] **Step 1: Write the complete solution**

Create `/Users/kalynnwillis/ai-office-hours-demo/solutions/demo_2_complete.py`:

```python
import pandas as pd
import matplotlib.pyplot as plt

# Plot humidity (RH_pct) over time for each unit as a separate colored line, with a legend and labeled axes

df = pd.read_csv('data/test_run_data.csv')
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

fig, ax = plt.subplots(figsize=(10, 6))
for unit, group in df.groupby('Unit'):
    ax.plot(group['Timestamp'], group['RH_pct'], marker='o', label=unit)

ax.set_xlabel('Time')
ax.set_ylabel('Humidity (%)')
ax.set_title('Humidity Over Time by Unit')
ax.legend()
ax.axhline(y=50, color='gray', linestyle='--', alpha=0.5, label='Setpoint (50%)')
plt.xticks(rotation=30, ha='right')
plt.tight_layout()
plt.savefig('humidity_chart.png')
plt.show()
print("Chart saved to humidity_chart.png")
```

- [ ] **Step 2: Run the solution and verify output**

```bash
cd /Users/kalynnwillis/ai-office-hours-demo
python solutions/demo_2_complete.py
```

Expected: a chart window opens showing 6 colored lines. `humidity_chart.png` is created in the project root.

- [ ] **Step 3: Commit**

```bash
git add solutions/demo_2_complete.py
git commit -m "Add solution script for Demo 2"
```

---

### Task 6: Starter script — Demo 3 (log summary)

**Files:**
- Create: `demo_3_log_summary.py`

- [ ] **Step 1: Write the starter file**

Create `/Users/kalynnwillis/ai-office-hours-demo/demo_3_log_summary.py`:

```python
# Read dehumidifier_serial.log and print all ERROR and WARN lines with their timestamps
```

- [ ] **Step 2: Verify the file is a single comment line**

```bash
cat /Users/kalynnwillis/ai-office-hours-demo/demo_3_log_summary.py
```

Expected: one line. No imports — this shows Copilot choosing its own approach.

- [ ] **Step 3: Commit**

```bash
git add demo_3_log_summary.py
git commit -m "Add starter script for Demo 3 (log summary)"
```

---

### Task 7: Solution script — Demo 3 (log summary)

**Files:**
- Create: `solutions/demo_3_complete.py`

- [ ] **Step 1: Write the complete solution**

Create `/Users/kalynnwillis/ai-office-hours-demo/solutions/demo_3_complete.py`:

```python
# Read dehumidifier_serial.log and print all ERROR and WARN lines with their timestamps

with open('data/dehumidifier_serial.log') as f:
    lines = f.readlines()

issues = [line.strip() for line in lines if 'ERROR' in line or 'WARN' in line]

print(f"Found {len(issues)} issue(s) in log:\n")
for issue in issues:
    print(issue)
```

- [ ] **Step 2: Run the solution and verify output**

```bash
cd /Users/kalynnwillis/ai-office-hours-demo
python solutions/demo_3_complete.py
```

Expected output:
```
Found 3 issue(s) in log:

[2026-06-01 10:36] WARN  RH 43% below comfort band (45-55)
[2026-06-01 11:02] ERROR E04 RH sensor read timeout, retry 1 of 3
[2026-06-01 11:02] ERROR E04 RH sensor read timeout, retry 2 of 3
```

- [ ] **Step 3: Commit**

```bash
git add solutions/demo_3_complete.py
git commit -m "Add solution script for Demo 3"
```

---

### Task 8: README speaker notes

**Files:**
- Create: `README.md`

- [ ] **Step 1: Write the README**

Create `/Users/kalynnwillis/ai-office-hours-demo/README.md`:

````markdown
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

  Unit            Timestamp  TempF  RH_pct Status
DH-004  2026-06-01 09:30   74.8      63  FAULT
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
````

- [ ] **Step 2: Verify README renders correctly**

```bash
cat /Users/kalynnwillis/ai-office-hours-demo/README.md | head -20
```

Expected: First 20 lines of the README visible and readable.

- [ ] **Step 3: Commit**

```bash
cd /Users/kalynnwillis/ai-office-hours-demo
git add README.md
git commit -m "Add README with speaker notes and setup instructions"
```

---

### Task 9: Push everything to GitHub

**Files:** None (git operation only)

- [ ] **Step 1: Verify all files are committed**

```bash
cd /Users/kalynnwillis/ai-office-hours-demo
git status
```

Expected: `nothing to commit, working tree clean`

- [ ] **Step 2: Push to GitHub**

```bash
git push origin main
```

Expected: All commits pushed, no errors.

- [ ] **Step 3: Verify on GitHub**

```bash
gh repo view khwillis1/ai-office-hours-demo --web
```

Expected: Browser opens to the repo showing all files and the README rendered.
