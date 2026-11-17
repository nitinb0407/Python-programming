# MODULE 4 - LAB EXERCISE 2
# Student data manager using files.

file_name = "students.txt"
count = int(input("How many students? "))

with open(file_name, "a", encoding="utf-8") as file:
    for _ in range(count):
        name = input("Enter student name: ")
        roll = input("Enter roll number: ")
        file.write(f"{roll},{name}\n")

print("\nSaved student records:")
with open(file_name, "r", encoding="utf-8") as file:
    for record in file:
        roll, name = record.strip().split(",", 1)
        print("Roll No:", roll, "| Name:", name)

# SAMPLE INPUT
# How many students? 2
# Enter student name: Asha
# Enter roll number: 101
# Enter student name: Manoj
# Enter roll number: 102
# SAMPLE OUTPUT (when students.txt was initially empty)
# Roll No: 101 | Name: Asha
# Roll No: 102 | Name: Manoj
