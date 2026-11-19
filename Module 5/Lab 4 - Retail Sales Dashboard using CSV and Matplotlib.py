"""
MODULE 5 - LAB 4: RETAIL SALES DASHBOARD USING CSV AND MATPLOTLIB

Requirements:
    pip install matplotlib

Run this file from the Module 5 folder. If sales_data.csv is not present,
the program creates it with sample records.

Sample console output:
===== RETAIL SALES DASHBOARD =====
Total records: 6
Total sales: Rs. 7550.00
Product with highest sales: Laptop (Rs. 5000.00)
A chart window will open showing sales by product.

The chart is also saved as retail_sales_dashboard.png.
"""

import csv
import os
from collections import defaultdict
import matplotlib.pyplot as plt

CSV_FILE = os.path.join(os.path.dirname(__file__), "sales_data.csv")
CHART_FILE = os.path.join(os.path.dirname(__file__), "retail_sales_dashboard.png")

SAMPLE_DATA = [
    ["Date", "Product", "Quantity", "UnitPrice"],
    ["2026-01-02", "Laptop", 1, 5000],
    ["2026-01-03", "Mouse", 5, 300],
    ["2026-01-04", "Keyboard", 2, 750],
    ["2026-01-05", "Monitor", 1, 4000],
    ["2026-01-06", "Mouse", 3, 300],
    ["2026-01-07", "Keyboard", 1, 750],
]


def create_sample_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(SAMPLE_DATA)
        print("Sample sales_data.csv created.")


def load_sales():
    product_sales = defaultdict(float)
    total_sales = 0.0
    record_count = 0

    with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        required = {"Product", "Quantity", "UnitPrice"}
        if not required.issubset(reader.fieldnames or []):
            raise ValueError("CSV must contain Product, Quantity and UnitPrice columns.")

        for row in reader:
            product = row["Product"].strip()
            quantity = int(row["Quantity"])
            unit_price = float(row["UnitPrice"])
            if not product or quantity < 0 or unit_price < 0:
                raise ValueError("CSV contains an invalid product, quantity or price.")
            amount = quantity * unit_price
            product_sales[product] += amount
            total_sales += amount
            record_count += 1

    return product_sales, total_sales, record_count


def display_dashboard(product_sales, total_sales, record_count):
    print("\n===== RETAIL SALES DASHBOARD =====")
    print(f"Total records: {record_count}")
    print(f"Total sales: Rs. {total_sales:.2f}")

    if not product_sales:
        print("No sales records found.")
        return

    best_product = max(product_sales, key=product_sales.get)
    print(f"Product with highest sales: {best_product} "
          f"(Rs. {product_sales[best_product]:.2f})")

    products = list(product_sales.keys())
    amounts = list(product_sales.values())

    plt.figure(figsize=(9, 5))
    bars = plt.bar(products, amounts)
    plt.title("Retail Sales by Product")
    plt.xlabel("Product")
    plt.ylabel("Sales Amount (Rs.)")
    plt.grid(axis="y", linestyle="--", alpha=0.4)
    plt.bar_label(bars, fmt="Rs. %.0f")
    plt.tight_layout()
    plt.savefig(CHART_FILE)
    print(f"Chart saved as: {CHART_FILE}")
    plt.show()


def main():
    print("===== RETAIL SALES DASHBOARD =====")
    try:
        create_sample_csv()
        product_sales, total_sales, record_count = load_sales()
        display_dashboard(product_sales, total_sales, record_count)
    except (OSError, ValueError, KeyError) as error:
        print(f"Unable to create dashboard: {error}")


if __name__ == "__main__":
    main()
