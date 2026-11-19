# Lab 2: Library Management System

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False


class Library:
    def __init__(self):
        self.books = [
            Book("Python Programming", "John Smith"),
            Book("Data Structures", "Anita Rao"),
            Book("Computer Networks", "David Miller")
        ]

    def display_books(self):
        print("\n--- LIBRARY BOOKS ---")
        for number, book in enumerate(self.books, start=1):
            status = "Borrowed" if book.is_borrowed else "Available"
            print(f"{number}. {book.title} by {book.author} - {status}")

    def add_book(self, title, author):
        self.books.append(Book(title, author))
        print("Book added successfully.")

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.is_borrowed:
                    print("This book is already borrowed.")
                else:
                    book.is_borrowed = True
                    print(f"You borrowed '{book.title}'.")
                return
        print("Book not found.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.is_borrowed:
                    print("This book was not borrowed.")
                else:
                    book.is_borrowed = False
                    print(f"'{book.title}' returned successfully.")
                return
        print("Book not found.")


def main():
    library = Library()

    while True:
        print("\n--- LIBRARY MENU ---")
        print("1. Display books")
        print("2. Add book")
        print("3. Borrow book")
        print("4. Return book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            library.display_books()
        elif choice == "2":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            library.add_book(title, author)
        elif choice == "3":
            title = input("Enter book title to borrow: ")
            library.borrow_book(title)
        elif choice == "4":
            title = input("Enter book title to return: ")
            library.return_book(title)
        elif choice == "5":
            print("Exiting Library Management System.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
