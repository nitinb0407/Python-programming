# Lab 2: Programs using variables, operators, and input/output

name = input("Enter your name: ")
age = int(input("Enter your age: "))
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\n--- Student Details ---")
print("Name:", name)
print("Age:", age)

print("\n--- Arithmetic Operations ---")
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

if num2 != 0:
    print("Division:", num1 / num2)
else:
    print("Division: Cannot divide by zero")

print("Remainder:", num1 % num2 if num2 != 0 else "Not possible")
