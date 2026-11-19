# MODULE 4 - MINI PROJECT
# JSON-based log file analyzer.
# Create sample.log with the sample lines below before running.

import json
from collections import Counter

file_name = input("Enter log file name: ")
levels = Counter()

try:
    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            upper_line = line.upper()
            for level in ("INFO", "WARNING", "ERROR"):
                if level in upper_line:
                    levels[level] += 1
                    break

    summary = dict(levels)
    with open("log_summary.json", "w", encoding="utf-8") as file:
        json.dump(summary, file, indent=4)

    print("Log summary:")
    print(json.dumps(summary, indent=4))
    print("Summary saved to log_summary.json")
except FileNotFoundError:
    print("Log file not found.")

# SAMPLE FILE (sample.log)
# INFO: Application started
# WARNING: Low disk space
# ERROR: Unable to connect
# INFO: User logged in
# SAMPLE INPUT
# Enter log file name: sample.log
# SAMPLE OUTPUT
# {
#     "INFO": 2,
#     "WARNING": 1,
#     "ERROR": 1
# }
# Summary saved to log_summary.json
