# MODULE 5 - MINI PROJECT
# Retail sales dashboard using CSV and matplotlib.
# Create sales.csv with columns Product,Sales before running.
# Install matplotlib: python -m pip install matplotlib

import csv
import matplotlib.pyplot as plt

products = []
sales = []

with open("sales.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        products.append(row["Product"])
        sales.append(float(row["Sales"]))

print("Retail Sales Report")
for product, amount in zip(products, sales):
    print(product, "- Rs.", f"{amount:.2f}")
print("Total sales: Rs.", f"{sum(sales):.2f}")

plt.bar(products, sales)
plt.title("Retail Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales (Rs.)")
plt.tight_layout()
plt.show()

# SAMPLE FILE (sales.csv)
# Product,Sales
# Pen,1200
# Book,2500
# Bag,4000
# SAMPLE OUTPUT
# Retail Sales Report
# Pen - Rs. 1200.00
# Book - Rs. 2500.00
# Bag - Rs. 4000.00
# Total sales: Rs. 7700.00
# A bar chart is displayed for the three products.
