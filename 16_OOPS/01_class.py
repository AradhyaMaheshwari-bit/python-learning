# Class: Blueprint or template for creating an object
# it defines what the object will be like, what data it will hold and what actions it can perform
# Object: Specific instance created from the class
# each object has its own unique set of data.

class Employee:
    company = "HP"

    def get_salary(self):  # self is important here because self is a way to reference the object of the class which is being created
        # print(self)
        return 34000

e = Employee()        # An object of class Employee is created here
print(e.get_salary()) # Employee e's get salary method is called

e2 = Employee()
print(e2.get_salary())
