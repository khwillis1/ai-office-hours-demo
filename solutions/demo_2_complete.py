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
