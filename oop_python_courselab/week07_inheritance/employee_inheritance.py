class Employee_nbs:
    def __init__(self_nbs, name_nbs, salary_nbs):
        self_nbs.name_nbs = name_nbs
        self_nbs.salary_nbs = salary_nbs

class Manager_nbs(Employee_nbs):
    def __init__(self_nbs, name_nbs, salary_nbs, department_nbs):
        super().__init__(name_nbs, salary_nbs)
        self_nbs.department_nbs = department_nbs

    def display_manager_nbs(self_nbs):
        print("Name:", self_nbs.name_nbs)
        print("Salary:", self_nbs.salary_nbs)
        print("Department:", self_nbs.department_nbs)

manager1_nbs = Manager_nbs("John", 50000, "IT")
manager1_nbs.display_manager_nbs()

#Nicole Sambile