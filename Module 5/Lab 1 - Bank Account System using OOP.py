"""
MODULE 5 - LAB 1: BANK ACCOUNT SYSTEM USING OOP

Sample run:
===== BANK ACCOUNT SYSTEM =====
1. Deposit
2. Withdraw
3. Check Balance
4. Exit
Enter your choice: 1
Enter deposit amount: 500
Rs.500.00 deposited successfully.
Current balance: Rs.1500.00

Starting balance for this sample: Rs.1000.00
"""

class BankAccount:
    def __init__(self, account_holder, account_number, balance=0.0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Please enter an amount greater than zero.")
        else:
            self.balance += amount
            print(f"Rs.{amount:.2f} deposited successfully.")
            print(f"Current balance: Rs.{self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Please enter an amount greater than zero.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Rs.{amount:.2f} withdrawn successfully.")
            print(f"Current balance: Rs.{self.balance:.2f}")

    def display_balance(self):
        print(f"Account holder: {self.account_holder}")
        print(f"Account number: {self.account_number}")
        print(f"Available balance: Rs.{self.balance:.2f}")


def main():
    print("===== BANK ACCOUNT SYSTEM =====")
    name = input("Enter account holder name: ")
    number = input("Enter account number: ")
    account = BankAccount(name, number, 1000.0)

    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                account.deposit(float(input("Enter deposit amount: ")))
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "2":
            try:
                account.withdraw(float(input("Enter withdrawal amount: ")))
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "3":
            account.display_balance()
        elif choice == "4":
            print("Thank you for using the Bank Account System.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
