"""Lab 2: Student Data Manager Using Files
Stores student records in students.txt and supports add, view, and search.
Each record is stored as: roll_number,name,marks
"""
from pathlib import Path

DATA_FILE = Path(__file__).with_name("students.txt")


def load_students():
    students = []
    if DATA_FILE.exists():
        for line in DATA_FILE.read_text(encoding="utf-8").splitlines():
            fields = line.split(",", 2)
            if len(fields) == 3:
                try:
                    students.append({
                        "roll": fields[0],
                        "name": fields[1],
                        "marks": float(fields[2])
                    })
                except ValueError:
                    continue
    return students


def save_students(students):
    lines = [
        f'{s["roll"]},{s["name"]},{s["marks"]}'
        for s in students
    ]
    DATA_FILE.write_text("\n".join(lines) + ("\n" if lines else ""),
                         encoding="utf-8")


def add_student(students):
    roll = input("Enter roll number: ").strip()
    if any(s["roll"] == roll for s in students):
        print("A student with this roll number already exists.")
        return
    name = input("Enter student name: ").strip().replace(",", " ")
    try:
        marks = float(input("Enter marks (0-100): "))
        if not 0 <= marks <= 100:
            raise ValueError
    except ValueError:
        print("Please enter valid marks between 0 and 100.")
        return
    students.append({"roll": roll, "name": name, "marks": marks})
    save_students(students)
    print("Student record saved successfully.")


def view_students(students):
    print("\n--------- STUDENT RECORDS ---------")
    if not students:
        print("No student records found.")
    else:
        print(f'{"Roll No.":<12}{"Name":<22}{"Marks":>8}')
        print("-" * 42)
        for s in students:
            print(f'{s["roll"]:<12}{s["name"]:<22}{s["marks"]:>8.2f}')
    print("-----------------------------------")


def search_student(students):
    roll = input("Enter roll number to search: ").strip()
    for s in students:
        if s["roll"] == roll:
            print(f'Found: {s["roll"]} | {s["name"]} | {s["marks"]:.2f} marks')
            return
    print("Student not found.")


def main():
    students = load_students()
    while True:
        print("\n===== STUDENT DATA MANAGER =====")
        print("1. Add student")
        print("2. View all students")
        print("3. Search student")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student(students)
            students = load_students()
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            print("Exiting Student Data Manager.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
