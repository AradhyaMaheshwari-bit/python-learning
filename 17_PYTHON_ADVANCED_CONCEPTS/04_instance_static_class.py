class Employee:
    company = "HP"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Instance method (Default)
    def print_info(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

    # Static Method: does not require self and self is not automatically passed when we call the function
    # we use it when we want no association with instance attributes
    @staticmethod
    def sum(a,b):
        return a+b

    # Class Method
    @classmethod
    def print_company(cls):
        print(cls.company)

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

e1 = Employee("Jack", 3455)
e2 = Employee("Jill", 34355)
print(Employee.company)
print(e1.company)
# print(Employee.name)
e1.print_info()
e2.print_info()

print(e2.sum(5 , 23))
e1.print_company()
e1.change_company("Acer")
e1.print_company()
print(Employee.company)
