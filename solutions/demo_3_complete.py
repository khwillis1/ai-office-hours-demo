# Read dehumidifier_serial.log and print all ERROR and WARN lines with their timestamps

with open('data/dehumidifier_serial.log') as f:
    lines = f.readlines()

issues = [line.strip() for line in lines if 'ERROR' in line or 'WARN' in line]

print(f"Found {len(issues)} issue(s) in log:\n")
for issue in issues:
    print(issue)
