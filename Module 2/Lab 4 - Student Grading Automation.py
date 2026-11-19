# Lab 4: Student Grading Automation

name = input("Enter student name: ")
subjects = int(input("Enter number of subjects: "))

if subjects <= 0:
    print("Number of subjects must be greater than zero.")
else:
    total = 0
    valid = True

    for i in range(1, subjects + 1):
        mark = float(input(f"Enter marks for subject {i} (0-100): "))
        if mark < 0 or mark > 100:
            print("Invalid marks. Marks must be between 0 and 100.")
            valid = False
            break
        total += mark

    if valid:
        average = total / subjects

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

        print("\n------ STUDENT RESULT ------")
        print("Student Name:", name)
        print("Total Marks:", total, "/", subjects * 100)
        print("Average:", round(average, 2), "%")
        print("Grade:", grade)
        print("Result:", "Pass" if average >= 40 else "Needs Improvement")
        print("----------------------------")
