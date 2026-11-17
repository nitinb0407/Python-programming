# MODULE 2 - MINI PROJECT
# Attendance tracker.

students = ["Anu", "Bala", "Charan"]
attendance = {}
for student in students:
    status = input(f"Is {student} present? (P/A): ").strip().upper()
    attendance[student] = "Present" if status == "P" else "Absent"

print("\nAttendance Report")
for student, status in attendance.items():
    print(student, "-", status)
present = sum(status == "Present" for status in attendance.values())
print("Present:", present)
print("Absent:", len(students) - present)

# SAMPLE INPUT
# Is Anu present? (P/A): P
# Is Bala present? (P/A): A
# Is Charan present? (P/A): P
# SAMPLE OUTPUT
# Attendance Report
# Anu - Present
# Bala - Absent
# Charan - Present
# Present: 2
# Absent: 1
