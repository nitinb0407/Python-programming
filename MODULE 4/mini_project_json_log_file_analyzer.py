# MODULE 4 - MINI PROJECT
# JSON-Based Log File Analyzer
# Reads log records from log.json and displays a summary by log level.

import json
from collections import Counter

FILE_NAME = "log.json"

try:
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        logs = json.load(file)

    if not isinstance(logs, list):
        raise ValueError("The JSON file must contain a list of log records.")

    level_counts = Counter()
    error_messages = []

    for entry in logs:
        level = entry.get("level", "UNKNOWN").upper()
        level_counts[level] += 1

        if level == "ERROR":
            error_messages.append(entry.get("message", "No message available"))

    print("\n========== JSON LOG FILE ANALYZER ==========")
    print("Log file:", FILE_NAME)
    print("Total log entries:", len(logs))

    print("\nLog Level Summary:")
    for level in ("INFO", "WARNING", "ERROR", "DEBUG", "UNKNOWN"):
        if level_counts[level] > 0:
            print(f"{level}: {level_counts[level]}")

    print("\nError Details:")
    if error_messages:
        for number, message in enumerate(error_messages, start=1):
            print(f"{number}. {message}")
    else:
        print("No errors found.")

    summary = {
        "total_entries": len(logs),
        "level_counts": dict(level_counts),
        "total_errors": len(error_messages),
        "error_messages": error_messages
    }

    with open("log_summary.json", "w", encoding="utf-8") as output_file:
        json.dump(summary, output_file, indent=4)

    print("\nAnalysis completed successfully.")
    print("Summary saved to log_summary.json")

except FileNotFoundError:
    print("Error: log.json file was not found.")
except json.JSONDecodeError:
    print("Error: log.json does not contain valid JSON.")
except (ValueError, AttributeError) as error:
    print("Error:", error)


# SAMPLE OUTPUT
#
# ========== JSON LOG FILE ANALYZER ==========
# Log file: log.json
# Total log entries: 6
#
# Log Level Summary:
# INFO: 2
# WARNING: 1
# ERROR: 2
# DEBUG: 1
#
# Error Details:
# 1. Database connection failed
# 2. Payment processing failed
#
# Analysis completed successfully.
# Summary saved to log_summary.json
