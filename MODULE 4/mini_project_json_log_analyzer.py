# MODULE 4 - MINI PROJECT
# JSON-Based Log File Analyzer
# Reads log entries from a JSON file and counts INFO, WARNING, and ERROR messages.

import json
from collections import Counter

file_name = "json_sample.log"
counts = Counter()

try:
    with open(file_name, "r", encoding="utf-8") as file:
        logs = json.load(file)

    for entry in logs:
        level = entry.get("level", "UNKNOWN").upper()
        counts[level] += 1

    summary = dict(counts)

    print("JSON Log File Analysis")
    print("----------------------")
    print("Total log entries:", len(logs))
    print("Log level summary:")
    print(json.dumps(summary, indent=4))

    with open("json_log_summary.json", "w", encoding="utf-8") as file:
        json.dump(summary, file, indent=4)

    print("Summary saved to json_log_summary.json")

except FileNotFoundError:
    print("JSON log file not found.")
except json.JSONDecodeError:
    print("Invalid JSON format in the log file.")


# SAMPLE INPUT FILE: json_sample.log
# [
#     {"time": "09:00", "level": "INFO", "message": "Application started"},
#     {"time": "09:05", "level": "WARNING", "message": "Low disk space"},
#     {"time": "09:10", "level": "ERROR", "message": "Unable to connect"},
#     {"time": "09:15", "level": "INFO", "message": "User logged in"}
# ]
#
# SAMPLE OUTPUT
# JSON Log File Analysis
# ----------------------
# Total log entries: 4
# Log level summary:
# {
#     "INFO": 2,
#     "WARNING": 1,
#     "ERROR": 1
# }
# Summary saved to json_log_summary.json
