"""Lab 3: Read employees.csv and calculate gross, deductions and net pay."""
import csv
from pathlib import Path
CSV_FILE = Path(__file__).with_name("employees.csv")

def calculate_pay(hours, rate, deduction_percent):
    regular = min(hours, 40)
    overtime = max(hours - 40, 0)
    gross = regular * rate + overtime * rate * 1.5
    deduction = gross * deduction_percent / 100
    return gross, deduction, gross - deduction

def main():
    if not CSV_FILE.exists():
        print(f"File not found: {CSV_FILE.name}")
        return
    print("\n================ PAYROLL REPORT ================")
    print(f"{'Employee':<18}{'Hours':>8}{'Gross':>12}{'Deduction':>12}{'Net Pay':>12}")
    print("-" * 62)
    total_net = 0.0
    try:
        with CSV_FILE.open("r", newline="", encoding="utf-8") as file:
            for row in csv.DictReader(file):
                hours = float(row["hours"])
                rate = float(row["hourly_rate"])
                pct = float(row["deduction_percent"])
                gross, deduction, net = calculate_pay(hours, rate, pct)
                total_net += net
                print(f"{row['name']:<18}{hours:>8.1f}{gross:>12.2f}{deduction:>12.2f}{net:>12.2f}")
    except (KeyError, ValueError) as error:
        print(f"Invalid CSV data: {error}")
        return
    print("-" * 62)
    print(f"{'Total net payroll:':<50}{total_net:>12.2f}")

if __name__ == "__main__":
    main()
