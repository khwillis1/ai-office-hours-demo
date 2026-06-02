import pandas as pd

# Load test_run_data.csv and print a summary of any FAULT rows, including which unit and when

df = pd.read_csv('data/test_run_data.csv')
faults = df[df['Status'] == 'FAULT']

if faults.empty:
    print("No faults found.")
else:
    print(f"Found {len(faults)} fault(s):\n")
    print(faults[['Unit', 'Timestamp', 'TempF', 'RH_pct', 'Status']].to_string(index=False))
