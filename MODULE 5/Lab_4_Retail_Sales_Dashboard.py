# Lab 4: Retail Sales Dashboard Using CSV and Matplotlib
# Objective: To read retail sales data from a CSV file and visualize
# the data using line graphs and bar charts.

import csv
import matplotlib.pyplot as plt

# Read retail sales data from the CSV file
products = []
sales = []

with open("sales.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        products.append(row["Product"])
        sales.append(float(row["Sales"]))

# Display the sales report
print("RETAIL SALES REPORT")
print("-------------------")

for product, amount in zip(products, sales):
    print(f"{product}: Rs. {amount:.2f}")

total_sales = sum(sales)
average_sales = total_sales / len(sales) if sales else 0

print("-------------------")
print(f"Total Sales: Rs. {total_sales:.2f}")
print(f"Average Sales: Rs. {average_sales:.2f}")

# Create a line graph
plt.figure(figsize=(8, 5))
plt.plot(products, sales, marker="o", linestyle="-")
plt.title("Retail Sales - Line Graph")
plt.xlabel("Product")
plt.ylabel("Sales (Rs.)")
plt.grid(True)
plt.tight_layout()

# Create a bar chart
plt.figure(figsize=(8, 5))
plt.bar(products, sales)
plt.title("Retail Sales - Bar Chart")
plt.xlabel("Product")
plt.ylabel("Sales (Rs.)")
plt.tight_layout()

# Display both graphs
plt.show()


# SAMPLE INPUT (sales.csv)
# Product,Sales
# Pen,1200
# Book,2500
# Bag,4000
#
# SAMPLE OUTPUT (console)
# RETAIL SALES REPORT
# -------------------
# Pen: Rs. 1200.00
# Book: Rs. 2500.00
# Bag: Rs. 4000.00
# -------------------
# Total Sales: Rs. 7700.00
# Average Sales: Rs. 2566.67
#
# Two graph windows are displayed:
# 1. A line graph showing sales for Pen, Book and Bag.
# 2. A bar chart comparing sales for Pen, Book and Bag.
#
# Install Matplotlib before running:
# python -m pip install matplotlib
#
# Keep sales.csv in the same folder as this Python file.
