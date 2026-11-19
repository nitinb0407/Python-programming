# Lab Exercise 1: Contact Book using Lists and Dictionaries

contacts = []

def add_contact():
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()

    if not name or not phone:
        print("Name and phone number are required.")
        return

    contacts.append({"name": name, "phone": phone, "email": email})
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts saved.")
        return

    print("\n--- CONTACT LIST ---")
    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. {contact['name']} | {contact['phone']} | {contact['email']}")

def search_contact():
    search_name = input("Enter name to search: ").strip().lower()
    found = False

    for contact in contacts:
        if search_name in contact["name"].lower():
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            found = True

    if not found:
        print("Contact not found.")

while True:
    print("\nCONTACT BOOK")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        print("Thank you for using Contact Book!")
        break
    else:
        print("Invalid choice. Please try again.")
