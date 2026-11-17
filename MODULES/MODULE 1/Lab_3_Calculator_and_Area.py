# MODULE 1 - LAB EXERCISE 3
# Simple calculator and area calculation programs.

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operator = input("Choose operation (+, -, *, /): ")

if operator == "+":
    print("Result:", a + b)
elif operator == "-":
    print("Result:", a - b)
elif operator == "*":
    print("Result:", a * b)
elif operator == "/":
    print("Result:", a / b if b != 0 else "Cannot divide by zero")
else:
    print("Invalid operator")

length = float(input("Enter rectangle length: "))
width = float(input("Enter rectangle width: "))
print("Area of rectangle:", length * width)

# SAMPLE INPUT
# Enter first number: 10
# Enter second number: 5
# Choose operation (+, -, *, /): *
# Enter rectangle length: 8
# Enter rectangle width: 4
# SAMPLE OUTPUT
# Result: 50.0
# Area of rectangle: 32.0
