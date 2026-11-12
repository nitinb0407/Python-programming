"""Lab 1: Log File Reader
Reads a log file and displays its entries with a summary by log level.
Place a file named sample.log in the same folder, or use the built-in sample.
"""
from pathlib import Path
from collections import Counter

LOG_FILE = Path(__file__).with_name("sample.log")


def create_sample_log():
    sample_lines = [
        "2026-11-10 09:00:00 INFO Application started",
        "2026-11-10 09:02:15 WARNING Disk space is getting low",
        "2026-11-10 09:03:40 ERROR Unable to connect to database",
        "2026-11-10 09:05:00 INFO Retrying database connection",
        "2026-11-10 09:05:30 INFO Connection successful",
    ]
    LOG_FILE.write_text("\n".join(sample_lines) + "\n", encoding="utf-8")


def main():
    if not LOG_FILE.exists():
        print("sample.log not found. Creating a sample log file...")
        create_sample_log()

    lines = LOG_FILE.read_text(encoding="utf-8").splitlines()
    counts = Counter()

    print("\n========== LOG FILE READER ==========")
    print(f"File: {LOG_FILE.name}\n")
    for line in lines:
        print(line)
        parts = line.split()
        if len(parts) >= 3:
            counts[parts[2]] += 1

    print("\n---------- LOG SUMMARY ----------")
    print(f"Total entries : {len(lines)}")
    for level in ("INFO", "WARNING", "ERROR"):
        print(f"{level:<14}: {counts[level]}")
    print("---------------------------------")


if __name__ == "__main__":
    main()
