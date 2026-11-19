# Lab 4: Unit converter and simple bill generator

print("UNIT CONVERTER")
print("1. Kilometres to Miles")
print("2. Celsius to Fahrenheit")
choice = input("Choose conversion (1 or 2): ")

if choice == "1":
    km = float(input("Enter distance in kilometres: "))
    print("Distance in miles:", round(km * 0.621371, 2))
elif choice == "2":
    celsius = float(input("Enter temperature in Celsius: "))
    print("Temperature in Fahrenheit:", round((celsius * 9 / 5) + 32, 2))
else:
    print("Invalid conversion choice.")

print("\nSIMPLE BILL GENERATOR")
item = input("Enter item name: ")
quantity = int(input("Enter quantity: "))
price = float(input("Enter price per item (Rs.): "))

if quantity < 0 or price < 0:
    print("Quantity and price cannot be negative.")
else:
    total = quantity * price
    print("\n------ BILL ------")
    print("Item:", item)
    print("Quantity:", quantity)
    print("Price per item: Rs.", format(price, ".2f"))
    print("Total amount: Rs.", format(total, ".2f"))
    print("------------------")
