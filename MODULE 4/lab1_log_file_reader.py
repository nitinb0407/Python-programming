"""Lab 1: Read a log file and summarize log levels."""
from pathlib import Path
from collections import Counter

LOG_FILE = Path(__file__).with_name("sample.log")

def read_log_file(path):
    if not path.exists():
        print(f"File not found: {path.name}")
        return
    counts = Counter()
    print(f"\nReading: {path.name}\n" + "-" * 45)
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        print(line)
        parts = line.split(maxsplit=2)
        counts[parts[1].upper() if len(parts) > 1 else "UNKNOWN"] += 1
    print("\n===== LOG SUMMARY =====")
    print(f"Total entries: {sum(counts.values())}")
    for level, count in sorted(counts.items()):
        print(f"{level}: {count}")

if __name__ == "__main__":
    read_log_file(LOG_FILE)
