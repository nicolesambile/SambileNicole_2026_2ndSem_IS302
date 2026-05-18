from student import Student
import file_handler as fh

def add_student_nbs():
    try:
        student_id_nbs = input("Enter Student ID: ").strip()
        if not student_id_nbs:
            raise ValueError("Student ID cannot be empty.")
        name_nbs = input("Enter Name: ").strip()
        course_nbs = input("Enter Course: ").strip()
        student_nbs = Student(student_id_nbs, name_nbs, course_nbs)
        fh.save_student_nbs(student_nbs)
        print("Student added successfully")
    except Exception as e_nbs:
        print("Error:", e_nbs)

def search_student_nbs():
    search_id_nbs = input("Enter Student ID to search: ").strip()
    if not search_id_nbs:
        print("Invalid ID")
        return
    found = fh.find_student_by_id_nbs(search_id_nbs)
    if found:
        print("Student Found:")
        print(f"{found[0]} | {found[1]} | {found[2]}")
    else:
        print("Student not found")

def main_nbs():
    while True:
        print("\nSTUDENT INFORMATION SYSTEM")
        print("1 Add Student")
        print("2 View Students")
        print("3 Search Student")
        print("4 Exit")
        choice_nbs = input("Enter choice: ").strip()
        if choice_nbs == "1":
            add_student_nbs()
        elif choice_nbs == "2":
            fh.view_students_nbs()
        elif choice_nbs == "3":
            search_student_nbs()
        elif choice_nbs == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main_nbs()

#Nicole B. Sambile