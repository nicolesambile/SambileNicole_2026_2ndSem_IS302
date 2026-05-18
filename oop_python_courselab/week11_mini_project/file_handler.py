import os   

STUDENTS_FILE_NBS = os.path.join(os.path.dirname(__file__), "students.txt")

def save_student_nbs(student_nbs):
    try:
        with open(STUDENTS_FILE_NBS, "a", encoding_nbs="utf-8") as f:
            f.write(student_nbs.to_record())
    except Exception as e_nbs:
        print("Error saving student:", e_nbs)

def view_students_nbs():
    try:
        with open(STUDENTS_FILE_NBS, "r", encoding_nbs="utf-8") as f:
            lines_nbs = [line.strip() for line in f if line.strip()]
            if not lines_nbs:
                print("No records found.")
                return
            print("Student ID | Name | Course")
            for line in lines_nbs:
                student_id_nbs, name_nbs, course_nbs = line.split(",", 2)
                print(f"{student_id_nbs} | {name_nbs} | {course_nbs}")
    except FileNotFoundError:
        print("No records found.")

def find_student_by_id_nbs(search_id_nbs):
    try:
        with open(STUDENTS_FILE_NBS, "r", encoding_nbs="utf-8") as f:
            for line in f:
                if not line.strip():
                    continue
                student_id_nbs, name_nbs, course_nbs = line.strip().split(",", 2)
                if student_id_nbs == search_id_nbs:
                    return (student_id_nbs, name_nbs, course_nbs)
    except FileNotFoundError:
        return None
    return None

#Nicole B. Sambile