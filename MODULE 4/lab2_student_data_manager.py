"""Lab 2: Add and view student records stored in students.txt."""
from pathlib import Path
DATA_FILE = Path(__file__).with_name("students.txt")

def add_student():
    roll = input("Enter roll number: ").strip()
    name = input("Enter student name: ").strip()
    course = input("Enter course: ").strip()
    if not all((roll, name, course)):
        print("All fields are required.")
        return
    if DATA_FILE.exists():
        for line in DATA_FILE.read_text(encoding="utf-8").splitlines():
            if line.split("|", 1)[0] == roll:
                print("Roll number already exists.")
                return
    with DATA_FILE.open("a", encoding="utf-8") as file:
        file.write(f"{roll}|{name}|{course}\n")
    print("Student record saved.")

def view_students():
    if not DATA_FILE.exists() or not DATA_FILE.read_text(encoding="utf-8").strip():
        print("No student records found.")
        return
    print("\n===== STUDENT RECORDS =====")
    print(f"{'Roll No.':<12}{'Name':<22}Course")
    print("-" * 48)
    for line in DATA_FILE.read_text(encoding="utf-8").splitlines():
        parts = line.split("|")
        if len(parts) == 3:
            roll, name, course = parts
            print(f"{roll:<12}{name:<22}{course}")

def main():
    while True:
        print("\n===== STUDENT DATA MANAGER =====")
        print("1. Add student\n2. View students\n3. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
