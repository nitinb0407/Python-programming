class Library:
    def __init__(self):
        self.books = {
            "Python Basics": True,
            "Data Structures": True,
            "Computer Networks": True
        }

    def display_books(self):
        print("\nAvailable Books:")
        for book, available in self.books.items():
            status = "Available" if available else "Borrowed"
            print(f"- {book}: {status}")

    def add_book(self, book):
        if book in self.books:
            print("This book already exists in the library.")
        else:
            self.books[book] = True
            print(f'"{book}" added successfully.')

    def borrow_book(self, book):
        if book not in self.books:
            print("Book not found.")
        elif not self.books[book]:
            print("Sorry, this book is already borrowed.")
        else:
            self.books[book] = False
            print(f'You have borrowed "{book}".')

    def return_book(self, book):
        if book not in self.books:
            print("This book does not belong to the library.")
        elif self.books[book]:
            print("This book was not borrowed.")
        else:
            self.books[book] = True
            print(f'"{book}" returned successfully.')


library = Library()

while True:
    print("\n--- LIBRARY MANAGEMENT SYSTEM ---")
    print("1. Display Books")
    print("2. Add Book")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.display_books()
    elif choice == "2":
        title = input("Enter book title: ")
        library.add_book(title)
    elif choice == "3":
        title = input("Enter book title to borrow: ")
        library.borrow_book(title)
    elif choice == "4":
        title = input("Enter book title to return: ")
        library.return_book(title)
    elif choice == "5":
        print("Thank you for using the library system!")
        break
    else:
        print("Invalid choice. Please try again.")
