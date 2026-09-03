# MODULE 1 - Lab Exercise 2
# Variables, Operators, Input and Output

name = input("Enter your name: ")
age = int(input("Enter your age: "))
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\n--- Student Details ---")
print("Name:", name)
print("Age:", age)

print("\n--- Arithmetic Operators ---")
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2 if num2 != 0 else "Cannot divide by zero")
print("Floor Division:", num1 // num2 if num2 != 0 else "Cannot divide by zero")
print("Modulus:", num1 % num2 if num2 != 0 else "Cannot divide by zero")
print("Power:", num1 ** num2)

print("\n--- Comparison Operators ---")
print("num1 == num2:", num1 == num2)
print("num1 != num2:", num1 != num2)
print("num1 > num2:", num1 > num2)
print("num1 < num2:", num1 < num2)
print("num1 >= num2:", num1 >= num2)
print("num1 <= num2:", num1 <= num2)

print("\n--- Logical Operators ---")
print("Both numbers are positive:", num1 > 0 and num2 > 0)
print("At least one number is positive:", num1 > 0 or num2 > 0)
print("num1 is not positive:", not (num1 > 0))
