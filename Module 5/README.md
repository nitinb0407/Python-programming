# Module 5 - Python Programming Labs

This module contains four Python programs and the sample CSV data used by Lab 4.

## Lab list

1. **Lab 1 - Bank Account System using OOP**  
   File: `Lab 1 - Bank Account System using OOP.py`  
   Demonstrates classes, objects, constructors, deposits, withdrawals and balance checking. The account starts with a sample balance of Rs. 1,000.

2. **Lab 2 - Library Management System**  
   File: `Lab 2 - Library Management System.py`  
   Demonstrates adding, displaying, borrowing and returning books. Two sample books are loaded when the program starts.

3. **Lab 3 - Dice Simulator using Random Module**  
   File: `Lab 3 - Dice Simulator using Random Module.py`  
   Uses `random.randint(1, 6)` to simulate dice rolls and displays roll statistics.

4. **Lab 4 - Retail Sales Dashboard using CSV and Matplotlib**  
   File: `Lab 4 - Retail Sales Dashboard using CSV and Matplotlib.py`  
   Reads sales records from `sales_data.csv`, calculates total sales and product-wise sales, and creates a bar chart.

## How to run

Open a terminal in this folder and run the required file:

```bash
python "Lab 1 - Bank Account System using OOP.py"
python "Lab 2 - Library Management System.py"
python "Lab 3 - Dice Simulator using Random Module.py"
python "Lab 4 - Retail Sales Dashboard using CSV and Matplotlib.py"
```

For Lab 4, install Matplotlib once:

```bash
pip install matplotlib
```

## Sample outputs

### Lab 1 - Bank Account System

Starting balance: Rs. 1,000.00

```text
Enter your choice: 1
Enter deposit amount: 500
Rs.500.00 deposited successfully.
Current balance: Rs.1500.00
```

### Lab 2 - Library Management System

```text
----- BOOK LIST -----
ID: 101 | Title: Python Basics | Author: John | Available: Yes
ID: 102 | Title: Data Structures | Author: Mary | Available: Yes
```

### Lab 3 - Dice Simulator

The dice result is random and can differ on every run.

```text
Press Enter to roll the dice or type q to quit:
You rolled: 4
Press Enter to roll the dice or type q to quit: q
Total rolls: 1
Thanks for playing!
```

### Lab 4 - Retail Sales Dashboard

Using the included six-row sample CSV:

```text
===== RETAIL SALES DASHBOARD =====
Total records: 6
Total sales: Rs. 7550.00
Product with highest sales: Laptop (Rs. 5000.00)
Chart saved as: retail_sales_dashboard.png
```

The chart opens in a Matplotlib window and is saved as `retail_sales_dashboard.png` after the program runs.

**Note:** Sample outputs are illustrative. Dice results and menu interactions can vary depending on user input.
