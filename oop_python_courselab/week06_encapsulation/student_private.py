class Student_nbs:
    def __init__(self_nbs, name_nbs, student_id_nbs, gpa_nbs):
        self_nbs.__name = name_nbs
        self_nbs.__student_id = student_id_nbs
        self_nbs.__gpa = gpa_nbs

    def get_student_info_nbs(self_nbs):
        print("Name:", self_nbs.__name)
        print("Student ID:", self_nbs.__student_id)
        print("GPA:", self_nbs.__gpa)

student1_nbs = Student_nbs("Juan", "2023-001", 1.75)
student1_nbs.get_student_info_nbs()

#Nicole B. Sambile