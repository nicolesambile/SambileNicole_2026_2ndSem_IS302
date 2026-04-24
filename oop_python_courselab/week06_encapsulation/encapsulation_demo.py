class Person_nbs:
    def __init__(self_nbs, name_nbs, age_nbs):
        self_nbs.__name = name_nbs
        self_nbs.__age = age_nbs

    def get_name_nbs(self_nbs):
        return self_nbs.__name

    def get_age_nbs(self_nbs):
        return self_nbs.__age

p1_nbs = Person_nbs("Maria", 20)
print("Name:", p1_nbs.get_name_nbs())
print("Age:", p1_nbs.get_age_nbs())

#Nicole Sambile