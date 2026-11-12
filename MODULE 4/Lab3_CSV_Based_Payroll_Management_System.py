"""Lab 3: CSV-Based Payroll Management System
Reads employee details from employees.csv, calculates gross pay,
deductions, and net pay, then saves the result to payroll_report.csv.

CSV input columns: employee_id,name,basic_salary,allowance,deduction
"""
import csv
from pathlib import Path

FOLDER = Path(__file__).parent
INPUT_FILE = FOLDER / "employees.csv"
OUTPUT_FILE = FOLDER / "payroll_report.csv"


def create_sample_csv():
    rows = [
        ["employee_id", "name", "basic_salary", "allowance", "deduction"],
        ["E101", "Ananya", "30000", "5000", "2000"],
        ["E102", "Kiran", "25000", "3500", "1500"],
        ["E103", "Meera", "40000", "6000", "3000"],
    ]
    with INPUT_FILE.open("w", newline="", encoding="utf-8") as file:
        csv.writer(file).writerows(rows)


def main():
    if not INPUT_FILE.exists():
        print("employees.csv not found. Creating sample employee data...")
        create_sample_csv()

    payroll = []
    try:
        with INPUT_FILE.open("r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            required = {"employee_id", "name", "basic_salary", "allowance", "deduction"}
            if not required.issubset(reader.fieldnames or []):
                raise ValueError("CSV file is missing one or more required columns.")

            for row in reader:
                basic = float(row["basic_salary"])
                allowance = float(row["allowance"])
                deduction = float(row["deduction"])
                gross = basic + allowance
                net = gross - deduction
                payroll.append({
                    "employee_id": row["employee_id"],
                    "name": row["name"],
                    "basic_salary": f"{basic:.2f}",
                    "allowance": f"{allowance:.2f}",
                    "gross_salary": f"{gross:.2f}",
                    "deduction": f"{deduction:.2f}",
                    "net_salary": f"{net:.2f}",
                })
    except (ValueError, KeyError) as error:
        print(f"Could not process payroll: {error}")
        return

    fieldnames = [
        "employee_id", "name", "basic_salary", "allowance",
        "gross_salary", "deduction", "net_salary"
    ]
    with OUTPUT_FILE.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(payroll)

    print("\n====== CSV PAYROLL MANAGEMENT SYSTEM ======")
    print(f'{"ID":<8}{"Name":<12}{"Gross Pay":>13}{"Deduction":>13}{"Net Pay":>13}')
    print("-" * 59)
    for item in payroll:
        print(
            f'{item["employee_id"]:<8}{item["name"]:<12}'
            f'{float(item["gross_salary"]):>13.2f}'
            f'{float(item["deduction"]):>13.2f}'
            f'{float(item["net_salary"]):>13.2f}'
        )
    print("-" * 59)
    print(f"Employees processed: {len(payroll)}")
    print(f"Payroll report saved to: {OUTPUT_FILE.name}")


if __name__ == "__main__":
    main()
