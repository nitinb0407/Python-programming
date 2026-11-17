# MODULE 3 - LAB EXERCISE 1
# Contact book using lists and dictionaries.

contacts = []
while True:
    name = input("Enter contact name (or stop): ")
    if name.lower() == "stop":
        break
    phone = input("Enter phone number: ")
    contacts.append({"name": name, "phone": phone})

print("\nContact Book")
for contact in contacts:
    print(contact["name"], "-", contact["phone"])

# SAMPLE INPUT
# Enter contact name (or stop): Kavin
# Enter phone number: 9988776655
# Enter contact name (or stop): stop
# SAMPLE OUTPUT
# Contact Book
# Kavin - 9988776655
