# MODULE 2 - LAB EXERCISE 2
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
# Enter student name: Ravi
# Enter mark for subject 1: 85
# Enter mark for subject 2: 90
# Enter mark for subject 3: 80
# SAMPLE OUTPUT
# Student: Ravi
# Total: 255.0
# Average: 85.0
# Grade: B
