# AI Office Hours — Week 2: GitHub Copilot

Demo guide and speaker notes. ~20 minutes total.

Two things you'll show: **inline completions** (type a comment → Copilot writes the code) and **Copilot Chat** (paste something → ask a question → get an answer).

---

## Before You Start

- VS Code open with this folder (`code .`)
- Copilot icon visible in status bar (bottom right — should be spinning when active)
- Copilot Chat panel open: click the chat bubble icon in the left sidebar, or press `Cmd+Shift+I` (Mac) / `Ctrl+Shift+I` (Windows)
- Terminal open inside VS Code
- Run once to confirm data is there: `ls data/`

---

## Intro (2 min)

**Say:** *"Today I'm going to show you two things Copilot does that'll save you real time this week. First: write code from a plain-English comment — no googling, no Stack Overflow. Second: answer questions about code or data you paste into chat — no vendor call, no digging through docs."*

*"We're going to use actual dehumidifier test data so this isn't abstract."*

---

## PART 1 — Inline Completions (~10 min)

> **What this is:** You type a comment describing what you want. Copilot reads the context (your imports, your comment) and suggests the code. You press Tab to accept.

---

### Demo 1A — Find the Fault (5 min)

**Open:** `demo_1_find_faults.py`

**Say:** *"I've got a CSV with readings from 6 dehumidifier units. One of them threw a fault — I want to find it. Watch what happens when I just describe what I want."*

**Show the audience the file** — it's just imports and a comment. No code yet.

**Position your cursor** at the end of the comment line and press **Enter**.

**Wait** for Copilot to suggest code (grey ghost text). Press **Tab** to accept. It may come line by line — keep pressing Tab.

**Run it:**
```bash
python demo_1_find_faults.py
```

**Expected output:**
```
Unit: DH-004, Timestamp: 2026-06-01 09:30, TempF: 74.8, RH_pct: 63
```

**Say:** *"DH-004 faulted at 9:30 AM — temp 74.8°F, humidity 63%. Copilot wrote all of that from one comment. This is a 5-second task that used to take 5 minutes of looking up pandas syntax."*

**If Copilot doesn't cooperate:** Open `solutions/demo_1_complete.py` and run that instead. Pivot: *"Let me show you the finished version."*

---

### Demo 1B — Visualize Humidity Trends (5 min)

**Open:** `demo_2_humidity_chart.py`

**Say:** *"Now let's visualize humidity across all units. The data loading is already there — I'll trigger Copilot just for the chart."*

**Position cursor** at the end of line 8 (the second comment line) and press **Enter**.

**Wait for Copilot** to suggest the plotting code. Press **Tab** to accept line by line.

**Run it:**
```bash
python demo_2_humidity_chart.py
```

**Expected output:** A chart window opens with 6 colored lines, one per unit. `humidity_chart.png` is saved in the project root.

**Say:** *"Each line is a unit. You can immediately see which ones are running high. Copilot wrote the groupby loop, the axis labels, the legend — all from two comment lines."*

**If Copilot doesn't cooperate:** Open `solutions/demo_2_complete.py` and run that instead.

---

### Demo 1C — Read the Log File (5 min)

**Open:** `demo_3_log_summary.py`

**Say:** *"Same idea, but now with a raw serial log — no structured columns, just text. One comment, no imports given — watch what Copilot picks."*

**Position cursor** at the end of line 1 and press **Enter**.

**Wait for Copilot**. Press **Tab** to accept.

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

**Say:** *"There's a sensor that timed out twice in a row. Without this you're scrolling through the log manually. Copilot filtered it in one comment — and it chose to use plain file I/O because there were no imports to go off of."*

**If Copilot doesn't cooperate:** Open `solutions/demo_3_complete.py` and run that instead.

---

## PART 2 — Copilot Chat (~8 min)

> **What this is:** Open the Copilot Chat panel. Paste in data, code, or an error. Ask a question in plain English. Get an answer — no environment needed, no docs to dig through.

**Open the chat panel now** if it isn't open: `Cmd+Shift+I` or click the chat bubble in the left sidebar.

---

### Chat Demo 1 — Interrogate the Data (4 min)

**Say:** *"We found DH-004 faulted. Now let's use the chat to understand what that actually means — like asking a coworker."*

**Type this into the chat (copy-paste from here):**

```
My CSV has these columns: Unit, Timestamp, TempF, RH_pct, Status.
DH-004 has Status=FAULT at 2026-06-01 09:30 with TempF=74.8 and RH_pct=63.
The setpoint is 50% RH. What does an RH reading of 63% mean for this unit?
What are the most likely causes, and what should I check first?
```

**Wait for response**, then **follow up:**

```
What's a simple Python check I could add to flag any unit that's been above 60% RH for more than 2 consecutive readings?
```

**Say:** *"This is the 'second set of eyes' use case. You found the problem with the inline completion. Now you're using chat to understand it and figure out next steps — without picking up the phone."*

---

### Chat Demo 2 — Decode the Log Format (4 min)

**Say:** *"Here's one that comes up constantly: you've got a log or config file someone else wrote, and you need to pull specific fields out of it."*

**Type this into the chat:**

```
My device logs look like this:
[2026-06-01 10:23] TEMP=72.4F RH=48%
[2026-06-01 10:36] WARN  RH 43% below comfort band (45-55)
[2026-06-01 11:02] ERROR E04 RH sensor read timeout, retry 1 of 3

Write a regex that captures the timestamp, log level (INFO/WARN/ERROR), and the message from each line.
Then give me a Python snippet that reads a file and prints only ERROR and WARN lines with their timestamps.
```

**Say:** *"Give it a real sample line — that's the whole trick. It can't guess your format, but it can read one example and generalize. No environment needed — you paste the sample, copy the code, drop it in your script."*

---

## Prompt Tips + Cheat Sheet (2 min)

**Say:** *"One pattern makes the difference between a useful answer and a useless one: give it a real sample."*

**Say out loud or show on screen:**

| Bad | Good |
|-----|------|
| `"Help me parse my log file."` | `"Sample line: [2026-06-01 10:23] TEMP=72.4F RH=48%. Write a regex that captures timestamp, temp, and RH as numbers."` |

---

**Starter prompts — steal these:**

```
Write a regex to extract [fields] from lines like: [paste a sample line]
```
```
Explain what this code/config does, step by step: [paste it]
```
```
CSV columns are [list them]. Flag rows where [value] is outside [spec] and count failures per unit.
```
```
Decode this error and tell me the likely cause and fix: [paste the error]
```
```
What would I change in this code to [do X]? [paste the relevant section]
```

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Copilot shows no inline suggestion | Check the Copilot icon in the status bar — it should be spinning. Press `Alt+\` (Windows) or `Option+\` (Mac) to trigger manually. |
| Copilot suggests wrong code | Press Escape, slightly rephrase the comment, wait again. |
| Script errors on run | Open the matching `solutions/` file and run that instead. Pivot: *"Let me show you the finished version."* |
| Chat gives a generic answer | Add more context — paste a sample line, name the columns, state the rule. Specific in = specific out. |
| Chart doesn't open (Demo 2) | Run `pip install matplotlib` and try again. |
