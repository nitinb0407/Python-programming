# MODULE 2 - Mini Project
# Student Grading Automation

print("===== STUDENT GRADING AUTOMATION =====")

name = input("Enter student name: ")
marks = []

for i in range(1, 6):
    mark = float(input(f"Enter marks for Subject {i} (0-100): "))
    while mark < 0 or mark > 100:
        print("Marks must be between 0 and 100.")
        mark = float(input(f"Enter marks for Subject {i}: "))
    marks.append(mark)

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

status = "Pass" if average >= 40 else "Fail"

print("\n===== RESULT =====")
print("Student Name:", name)
print("Total Marks:", total, "/ 500")
print(f"Average: {average:.2f}%")
print("Grade:", grade)
print("Status:", status)
