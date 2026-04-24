class Employee_nbs:
    def __init__(self_nbs, name_nbs):
        self_nbs.__name = name_nbs
        self_nbs.__salary = 0

    def set_salary_nbs(self_nbs, salary_nbs):
        if salary_nbs > 0:
            self_nbs.__salary = salary_nbs

    def get_salary_nbs(self_nbs):
        return self_nbs.__salary

emp_nbs = Employee_nbs("Ana")
emp_nbs.set_salary_nbs(30000)
print("Salary:", emp_nbs.get_salary_nbs())

#Nicole Sambile