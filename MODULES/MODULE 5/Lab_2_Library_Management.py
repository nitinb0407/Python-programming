# MODULE 5 - LAB EXERCISE 2
# Library management system: add and search books.

books = []
count = int(input("How many books do you want to add? "))

for _ in range(count):
    title = input("Enter book title: ")
    author = input("Enter author: ")
    books.append({"title": title, "author": author})

search_title = input("Enter title to search: ").lower()
for book in books:
    if book["title"].lower() == search_title:
        print("Book found:", book["title"], "by", book["author"])
        break
else:
    print("Book not found.")

# SAMPLE INPUT
# How many books do you want to add? 2
# Enter book title: Python Basics
# Enter author: John
# Enter book title: Data Science
# Enter author: Meera
# Enter title to search: Python Basics
# SAMPLE OUTPUT
# Book found: Python Basics by John
