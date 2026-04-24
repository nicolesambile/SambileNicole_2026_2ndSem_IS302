class Person_nbs:
    def __init__(self_nbs, name_nbs, age_nbs):
        self_nbs.name_nbs = name_nbs
        self_nbs.age_nbs = age_nbs

class Student_nbs(Person_nbs):
    def __init__(self_nbs, name_nbs, age_nbs, course_nbs):
        super().__init__(name_nbs, age_nbs)
        self_nbs.course_nbs = course_nbs

    def display_student_nbs(self_nbs):
        print("Name:", self_nbs.name_nbs)
        print("Age:", self_nbs.age_nbs)
        print("Course:", self_nbs.course_nbs)

student1_nbs = Student_nbs("Maria", 20, "BSIS")
student1_nbs.display_student_nbs()

#Nicole Sambile