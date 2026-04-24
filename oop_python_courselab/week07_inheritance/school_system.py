class Person_nbs:
    def __init__(self_nbs, name_nbs, age_nbs):
        self_nbs.name_nbs = name_nbs
        self_nbs.age_nbs = age_nbs

    def display_info_nbs(self_nbs):
        print("Name:", self_nbs.name_nbs)
        print("Age:", self_nbs.age_nbs)

class Student_nbs(Person_nbs):
    def __init__(self_nbs, name_nbs, age_nbs, course_nbs):
        super().__init__(name_nbs, age_nbs)
        self_nbs.course_nbs = course_nbs

    def display_info_nbs(self_nbs):
        super().display_info_nbs()
        print("Course:", self_nbs.course_nbs)

class Teacher_nbs(Person_nbs):
    def __init__(self_nbs, name_nbs, age_nbs, subject_nbs):
        super().__init__(name_nbs, age_nbs)
        self_nbs.subject_nbs = subject_nbs

    def display_info_nbs(self_nbs):
        super().display_info_nbs()
        print("Subject:", self_nbs.subject_nbs)

# Example usage
student_nbs = Student_nbs("Maria", 20, "BSIS")
teacher_nbs = Teacher_nbs("Mr. Smith", 45, "Mathematics")

print("Student Info:")
student_nbs.display_info_nbs()
print("\nTeacher Info:")
teacher_nbs.display_info_nbs()

#Nicole Sambile