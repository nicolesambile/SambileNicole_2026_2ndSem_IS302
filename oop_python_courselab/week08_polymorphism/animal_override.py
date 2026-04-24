class Animal_nbs:
    def speak_nbs(self_nbs):
        print("Animal makes a sound")

class Dog_nbs(Animal_nbs):
    def speak_nbs(self_nbs):
        print("Dog barks")

class Cat_nbs(Animal_nbs):
    def speak_nbs(self_nbs):
        print("Cat meows")

animals_nbs = [Dog_nbs(), Cat_nbs()]
for animal_nbs in animals_nbs:
    animal_nbs.speak_nbs()

#Nicole Sambile