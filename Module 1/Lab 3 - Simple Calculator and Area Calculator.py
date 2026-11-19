# Lab 3: Simple calculator and area calculation programs

print("SIMPLE CALCULATOR")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operator = input("Enter operation (+, -, *, /): ")

if operator == "+":
    print("Result:", a + b)
elif operator == "-":
    print("Result:", a - b)
elif operator == "*":
    print("Result:", a * b)
elif operator == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator.")

print("\nAREA CALCULATOR")
print("1. Rectangle")
print("2. Circle")
choice = input("Choose a shape (1 or 2): ")

if choice == "1":
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    print("Area of rectangle:", length * width)
elif choice == "2":
    radius = float(input("Enter radius: "))
    print("Area of circle:", 3.14159 * radius * radius)
else:
    print("Invalid choice.")
