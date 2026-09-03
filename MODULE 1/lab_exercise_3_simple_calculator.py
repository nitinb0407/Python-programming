# MODULE 1 - Lab Exercise 3
# Simple Calculator

print("Simple Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice (1-4): "))
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    result = num1 + num2
elif choice == 2:
    result = num1 - num2
elif choice == 3:
    result = num1 * num2
elif choice == 4:
    if num2 == 0:
        print("Error: Cannot divide by zero.")
        result = None
    else:
        result = num1 / num2
else:
    print("Invalid choice.")
    result = None

if result is not None:
    print("Result:", result)
