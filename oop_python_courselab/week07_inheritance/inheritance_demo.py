class Animal_nbs:
    def __init__(self_nbs, name_nbs):
        self_nbs.name_nbs = name_nbs

    def speak(self_nbs):
        print(self_nbs.name_nbs, "makes a sound")

class Dog_nbs(Animal_nbs):
    def bark(self_nbs):
        print(self_nbs.name_nbs, "barks")

dog1_nbs = Dog_nbs("Buddy")
dog1_nbs.speak()
dog1_nbs.bark()

#Nicole Sambile