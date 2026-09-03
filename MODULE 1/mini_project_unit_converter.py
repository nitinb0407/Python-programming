# MODULE 1 - Mini Project
# Unit Converter

print("===== UNIT CONVERTER =====")
print("1. Kilometers to Miles")
print("2. Miles to Kilometers")
print("3. Celsius to Fahrenheit")
print("4. Fahrenheit to Celsius")
print("5. Kilograms to Pounds")
print("6. Pounds to Kilograms")
print("7. Meters to Feet")
print("8. Feet to Meters")

choice = int(input("Enter your choice (1-8): "))
value = float(input("Enter value to convert: "))

if choice == 1:
    result = value * 0.621371
    unit = "miles"
elif choice == 2:
    result = value * 1.609344
    unit = "kilometers"
elif choice == 3:
    result = (value * 9 / 5) + 32
    unit = "°F"
elif choice == 4:
    result = (value - 32) * 5 / 9
    unit = "°C"
elif choice == 5:
    result = value * 2.20462
    unit = "pounds"
elif choice == 6:
    result = value * 0.453592
    unit = "kilograms"
elif choice == 7:
    result = value * 3.28084
    unit = "feet"
elif choice == 8:
    result = value * 0.3048
    unit = "meters"
else:
    print("Invalid choice.")
    result = None

if result is not None:
    print(f"Converted value: {result:.2f} {unit}")
