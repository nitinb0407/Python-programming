# MODULE 5 - LAB EXERCISE 1
# Bank account system using OOP.

class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit successful.")
        else:
            print("Enter a positive amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful.")
        else:
            print("Insufficient balance or invalid amount.")

    def show_balance(self):
        print("Account holder:", self.name)
        print("Balance:", f"{self.balance:.2f}")


account = BankAccount(input("Account holder name: "),
                      float(input("Opening balance: ")))
account.deposit(float(input("Deposit amount: ")))
account.withdraw(float(input("Withdrawal amount: ")))
account.show_balance()

# SAMPLE INPUT
# Account holder name: Nithin
# Opening balance: 5000
# Deposit amount: 1500
# Withdrawal amount: 1000
# SAMPLE OUTPUT
# Deposit successful.
# Withdrawal successful.
# Account holder: Nithin
# Balance: 5500.00
