# MODULE 1 - MINI PROJECT
# Unit converter: kilometres to miles or Celsius to Fahrenheit.

print("1. Kilometres to miles")
print("2. Celsius to Fahrenheit")
choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    km = float(input("Enter distance in kilometres: "))
    print("Distance in miles:", round(km * 0.621371, 2))
elif choice == "2":
    celsius = float(input("Enter temperature in Celsius: "))
    print("Temperature in Fahrenheit:", round(celsius * 9 / 5 + 32, 2))
else:
    print("Invalid choice")

# SAMPLE INPUT
# Enter your choice (1 or 2): 1
# Enter distance in kilometres: 10
# SAMPLE OUTPUT
# Distance in miles: 6.21
