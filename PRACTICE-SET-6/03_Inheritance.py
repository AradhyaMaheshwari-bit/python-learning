class Animal:
    def __init__(self, name="N/A", breed="N/A"):
        self.name = name
        self.breed = breed
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        print("Bark!")


a = Animal()
a.sound()

d = Dog()
d.sound()

