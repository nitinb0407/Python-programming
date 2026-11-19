class BankAccount:
    def __init__(self, account_holder, balance=1000):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Please enter a valid deposit amount.")
        else:
            self.balance += amount
            print(f"Rs.{amount:.2f} deposited successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Please enter a valid withdrawal amount.")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Rs.{amount:.2f} withdrawn successfully.")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Available Balance: Rs.{self.balance:.2f}")


name = input("Enter account holder name: ")
account = BankAccount(name)

while True:
    print("\n--- BANK ACCOUNT MENU ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter amount to deposit: Rs."))
        account.deposit(amount)
    elif choice == "2":
        amount = float(input("Enter amount to withdraw: Rs."))
        account.withdraw(amount)
    elif choice == "3":
        account.display_balance()
    elif choice == "4":
        print("Thank you for using our banking system!")
        break
    else:
        print("Invalid choice. Please try again.")
