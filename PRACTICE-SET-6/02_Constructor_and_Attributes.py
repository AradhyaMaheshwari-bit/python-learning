class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_info(self):
        print(f"Name of the person is {self.name} and his age is {self.age}.")

a = Person("Rahul", 16)
a.get_info()
