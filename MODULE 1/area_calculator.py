# MODULE 1 - Lab Exercise 3
# Area Calculation Programs

import math

print("Area Calculator")
print("1. Circle")
print("2. Rectangle")
print("3. Triangle")
print("4. Square")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    radius = float(input("Enter radius: "))
    area = math.pi * radius ** 2
    print("Area of circle:", area)

elif choice == 2:
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    area = length * width
    print("Area of rectangle:", area)

elif choice == 3:
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    area = 0.5 * base * height
    print("Area of triangle:", area)

elif choice == 4:
    side = float(input("Enter side: "))
    area = side ** 2
    print("Area of square:", area)

else:
    print("Invalid choice.")
