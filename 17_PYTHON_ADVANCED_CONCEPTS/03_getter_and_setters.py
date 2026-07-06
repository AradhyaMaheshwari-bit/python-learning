class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property
    def first_name(self):                       # getter
        parts = self.name.split(" ")
        return parts[0]

    @first_name.setter
    def first_name(self, first):                # setter
        parts = self.name.split(" ")
        new_name = f"{first} {parts[1]}"
        self.name = new_name

e = Employee("Jack Doe", 34555)
# e.projects = 6
# print(e.projects)
# print(e.first_name())
# e.set_first_name("John")
# print(e.name)

print(e.first_name)
e.first_name = "John"
print(e.name)

