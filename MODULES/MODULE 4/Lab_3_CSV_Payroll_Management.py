# MODULE 4 - LAB EXERCISE 3
# CSV-based payroll management system.

import csv

count = int(input("Enter number of employees: "))
rows = []
for _ in range(count):
    name = input("Employee name: ")
    basic = float(input("Basic salary: "))
    allowance = float(input("Allowance: "))
    deduction = float(input("Deduction: "))
    net_salary = basic + allowance - deduction
    rows.append([name, basic, allowance, deduction, net_salary])

with open("payroll.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Basic", "Allowance", "Deduction", "Net Salary"])
    writer.writerows(rows)

print("\nPayroll Report")
for row in rows:
    print(row[0], "- Net Salary:", f"{row[4]:.2f}")
print("Payroll saved to payroll.csv")

# SAMPLE INPUT
# Enter number of employees: 1
# Employee name: Kumar
# Basic salary: 25000
# Allowance: 3000
# Deduction: 1000
# SAMPLE OUTPUT
# Payroll Report
# Kumar - Net Salary: 27000.00
# Payroll saved to payroll.csv
