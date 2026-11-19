"""
MODULE 5 - LAB 2: LIBRARY MANAGEMENT SYSTEM

Sample run:
===== LIBRARY MANAGEMENT SYSTEM =====
1. Add Book
2. Display Books
3. Borrow Book
4. Return Book
5. Exit
Enter your choice: 2

ID: 101 | Title: Python Basics | Author: John | Available: Yes
ID: 102 | Title: Data Structures | Author: Mary | Available: Yes

The program starts with two sample books.
"""

class Library:
    def __init__(self):
        self.books = {
            101: {"title": "Python Basics", "author": "John", "available": True},
            102: {"title": "Data Structures", "author": "Mary", "available": True}
        }

    def add_book(self, book_id, title, author):
        if book_id in self.books:
            print("A book with this ID already exists.")
            return
        self.books[book_id] = {
            "title": title, "author": author, "available": True
        }
        print("Book added successfully.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
            return
        print("\n----- BOOK LIST -----")
        for book_id, book in self.books.items():
            status = "Yes" if book["available"] else "No"
            print(f"ID: {book_id} | Title: {book['title']} | "
                  f"Author: {book['author']} | Available: {status}")

    def borrow_book(self, book_id):
        book = self.books.get(book_id)
        if book is None:
            print("Book ID not found.")
        elif not book["available"]:
            print("This book is already borrowed.")
        else:
            book["available"] = False
            print(f"You have borrowed '{book['title']}'.")

    def return_book(self, book_id):
        book = self.books.get(book_id)
        if book is None:
            print("Book ID not found.")
        elif book["available"]:
            print("This book was not borrowed.")
        else:
            book["available"] = True
            print(f"'{book['title']}' returned successfully.")


def main():
    library = Library()
    print("===== LIBRARY MANAGEMENT SYSTEM =====")

    while True:
        print("\n1. Add Book\n2. Display Books\n3. Borrow Book"
              "\n4. Return Book\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                book_id = int(input("Enter book ID: "))
                title = input("Enter book title: ")
                author = input("Enter author name: ")
                library.add_book(book_id, title, author)
            except ValueError:
                print("Book ID must be a number.")
        elif choice == "2":
            library.display_books()
        elif choice == "3":
            try:
                library.borrow_book(int(input("Enter book ID to borrow: ")))
            except ValueError:
                print("Book ID must be a number.")
        elif choice == "4":
            try:
                library.return_book(int(input("Enter book ID to return: ")))
            except ValueError:
                print("Book ID must be a number.")
        elif choice == "5":
            print("Thank you for using the Library Management System.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
