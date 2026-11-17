# MODULE 3 - MINI PROJECT
# Sales data analyzer.

sales = []
days = int(input("Enter number of sales days: "))
for day in range(1, days + 1):
    sales.append(float(input(f"Enter sales for day {day}: ")))

print("Total sales:", sum(sales))
print("Average daily sales:", round(sum(sales) / len(sales), 2))
print("Highest sales:", max(sales))
print("Lowest sales:", min(sales))

# SAMPLE INPUT
# Enter number of sales days: 4
# Enter sales for day 1: 1200
# Enter sales for day 2: 1500
# Enter sales for day 3: 900
# Enter sales for day 4: 1400
# SAMPLE OUTPUT
# Total sales: 5000.0
# Average daily sales: 1250.0
# Highest sales: 1500.0
# Lowest sales: 900.0
