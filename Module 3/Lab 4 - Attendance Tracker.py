# Lab Exercise 4: Attendance Tracker

attendance = {}

number_of_students = int(input("Enter number of students: "))
total_working_days = int(input("Enter total working days: "))

if number_of_students <= 0 or total_working_days <= 0:
    print("Please enter positive numbers for students and working days.")
else:
    for i in range(number_of_students):
        name = input(f"Enter name of student {i + 1}: ")
        present_days = int(input(f"Enter days present for {name}: "))

        if present_days < 0 or present_days > total_working_days:
            print("Invalid attendance count. Record skipped.")
            continue

        percentage = (present_days / total_working_days) * 100
        attendance[name] = {
            "present": present_days,
            "absent": total_working_days - present_days,
            "percentage": percentage
        }

    print("\n--------- ATTENDANCE REPORT ---------")
    if not attendance:
        print("No valid attendance records available.")
    else:
        for name, record in attendance.items():
            status = "Eligible" if record["percentage"] >= 75 else "Shortage"
            print(f"Name: {name}")
            print(f"Present: {record['present']} | Absent: {record['absent']}")
            print(f"Attendance: {record['percentage']:.2f}% | Status: {status}")
            print("-------------------------------------")
