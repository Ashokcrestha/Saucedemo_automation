import csv
from datetime import datetime

BUG_FILE = "reports/bug_report.csv"

def log_bug(test_name, issue, severity, priority):
    with open(BUG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now(),
            test_name,
            issue,
            severity,
            priority
        ])
