class Student_nbs:
    def __init__(self_nbs, student_id_nbs, name_nbs, course_nbs):
        self_nbs.student_id_nbs = student_id_nbs.strip()
        self_nbs.name_nbs = name_nbs.strip()
        self_nbs.course_nbs = course_nbs.strip()

    def display_info_nbs(self_nbs):
        print(f"{self_nbs.student_id_nbs} | {self_nbs.name_nbs} | {self_nbs.course_nbs}")

    def to_record_nbs(self_nbs):
        return f"{self_nbs.student_id_nbs},{self_nbs.name_nbs},{self_nbs.course_nbs}\n"

#Nicole B. Sambile