# Lab Exercise 2: Student Grading System

students = []

count = int(input("Enter number of students: "))

for i in range(count):
    print(f"\nStudent {i + 1}")
    name = input("Enter student name: ")
    marks = float(input("Enter marks (0-100): "))

    if marks < 0 or marks > 100:
        print("Invalid marks. Please enter marks between 0 and 100.")
        continue

    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 50:
        grade = "D"
    else:
        grade = "F"

    students.append({"name": name, "marks": marks, "grade": grade})

print("\n------ STUDENT GRADING REPORT ------")
if not students:
    print("No valid student records were entered.")
else:
    for student in students:
        result = "Pass" if student["marks"] >= 40 else "Fail"
        print(f"Name: {student['name']} | Marks: {student['marks']} | Grade: {student['grade']} | Result: {result}")
