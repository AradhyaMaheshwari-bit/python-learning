class Employee:
    company = "HP"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"The name is {self.name} and the salary is {self.salary}."

    def __repr__(self):
        return f"name: {self.name}\nsalary: {self.salary}"

    def __len__(self):
        return len(self.name)

    def __add__(self, other):
        return self.salary + other.salary

    def __sub__(self, other):
        return self.salary - other.salary

e1 = Employee("Harry", 43566)
e2 = Employee("John", 60000)

# print(e1.name, e2.salary)
# print(str(e1))
# print(repr(e1))
# print(e2)
# print(len(e1))

print(e1+e2)
print(e1-e2)
