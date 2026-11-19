# Lab Exercise 4: Student Grading Automation

print("STUDENT GRADING SYSTEM")

name = input("Enter student name: ")
marks = []

for subject in range(1, 4):
    while True:
        try:
            mark = float(input(f"Enter marks for subject {subject} (0-100): "))
            if 0 <= mark <= 100:
                marks.append(mark)
                break
            print("Marks must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")

total = sum(marks)
average = total / len(marks)

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

print("\n------ STUDENT REPORT ------")
print("Student Name:", name)
print("Total Marks:", total, "/", len(marks) * 100)
print("Average:", round(average, 2))
print("Grade:", grade)

if all(mark >= 35 for mark in marks):
    print("Result: PASS")
else:
    print("Result: FAIL")

print("----------------------------")
