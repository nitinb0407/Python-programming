import csv
import os
from collections import defaultdict
import matplotlib.pyplot as plt

CSV_FILE = "sales_data.csv"

# Create a sample CSV file if it is not already available.
if not os.path.exists(CSV_FILE):
    sample_rows = [
        ["Product", "Quantity", "Unit Price"],
        ["Laptop", 2, 25000],
        ["Mouse", 10, 400],
        ["Keyboard", 5, 900],
        ["Monitor", 2, 10000],
        ["Mouse", 5, 400],
        ["Laptop", 1, 25000]
    ]

    with open(CSV_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(sample_rows)

sales = defaultdict(float)
total_sales = 0

with open(CSV_FILE, "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["Product"]
        quantity = int(row["Quantity"])
        unit_price = float(row["Unit Price"])
        amount = quantity * unit_price

        sales[product] += amount
        total_sales += amount

print("--- RETAIL SALES REPORT ---")
for product, amount in sales.items():
    print(f"{product}: Rs.{amount:.2f}")

print(f"\nTotal Sales: Rs.{total_sales:.2f}")

if sales:
    top_product = max(sales, key=sales.get)
    print(f"Top Revenue Product: {top_product}")

    plt.figure(figsize=(8, 5))
    plt.bar(sales.keys(), sales.values())
    plt.title("Retail Sales by Product")
    plt.xlabel("Product")
    plt.ylabel("Sales (Rs.)")
    plt.tight_layout()
    plt.savefig("retail_sales_dashboard.png")
    plt.show()
    print("Dashboard saved as retail_sales_dashboard.png.")
else:
    print("No sales records found in the CSV file.")
