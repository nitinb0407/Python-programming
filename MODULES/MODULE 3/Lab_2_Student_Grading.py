# MODULE 3 - LAB EXERCISE 2
# Student grading system.

name = input("Enter student name: ")
marks = [float(input(f"Enter mark for subject {i}: ")) for i in range(1, 4)]
average = sum(marks) / len(marks)

if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "F"

print("Student:", name)
print("Total:", sum(marks))
print("Average:", round(average, 2))
print("Grade:", grade)

# SAMPLE INPUT
# Enter student name: Priya
# Enter mark for subject 1: 92
# Enter mark for subject 2: 88
# Enter mark for subject 3: 90
# SAMPLE OUTPUT
# Student: Priya
# Total: 270.0
# Average: 90.0
# Grade: A
