class Employee_nbs:
    def work_nbs(self_nbs):
        print("Employee performs tasks")

class Programmer_nbs(Employee_nbs):
    def work_nbs(self_nbs):
        print("Programmer writes code")

class Designer_nbs(Employee_nbs):
    def work_nbs(self_nbs):
        print("Designer creates UI designs")

employees_nbs = [Programmer_nbs(), Designer_nbs()]
for emp_nbs in employees_nbs:
    emp_nbs.work_nbs()

#Nicole Sambile