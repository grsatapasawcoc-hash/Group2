# Student Information Tracker (Simple Version)
# Language: Python
# Type: Terminal-based System (No database)

students = []  # List to store student records

def add_student():
    print("\n--- Add Student ---")
    student = {}
    student["id"] = input("Student ID: ")
    student["name"] = input("Full Name: ")
    student["course"] = input("Course: ")
    student["year"] = input("Year Level: ")
    students.append(student)
    print(" Student added successfully!")

def view_students():
    print("\n--- Student List ---")
    if not students:
        print("No students found.")
    else:
        for s in students:
            print(f"ID: {s['id']}, Name: {s['name']}, Course: {s['course']}, Year: {s['year']}")

def search_student():
    print("\n--- Search Student ---")
    sid = input("Enter Student ID to search: ")
    found = False
    for s in students:
        if s["id"] == sid:
            print(f" Found: {s['name']} - {s['course']} ({s['year']})")
            found = True
            break
    if not found:
        print(" Student not found.")

def update_student():
    print("\n--- Update Student ---")
    sid = input("Enter Student ID to update: ")
    for s in students:
        if s["id"] == sid:
            print("Leave blank to keep current value.")
            name = input(f"New Name ({s['name']}): ") or s["name"]
            course = input(f"New Course ({s['course']}): ") or s["course"]
            year = input(f"New Year Level ({s['year']}): ") or s["year"]
            s.update({"name": name, "course": course, "year": year})
            print(" Student information updated.")
            return
    print(" Student not found.")

def delete_student():
    print("\n--- Delete Student ---")
    sid = input("Enter Student ID to delete: ")
    for s in students:
        if s["id"] == sid:
            students.remove(s)
            print(" Student deleted.")
            return
    print(" Student not found.")

def main_menu():
    while True:
        print("\n=== Student Information Tracker ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("0. Exit")
        
        choice = input(" Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "0":
            print(" Goodbye!")
            break
        else:
            print(" Invalid choice, please try again.")

# Run the system
main_menu()