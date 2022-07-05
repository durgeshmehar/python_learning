class Animal:
    animalType="Mammal"

class Pet(Animal):
    color="White"

class Dog(Pet):
    @staticmethod
    def bark():
        print("Bow bow")

d1=Dog()
d1.bark()