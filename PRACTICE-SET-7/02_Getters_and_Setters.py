class Employee:
    def __init__(self,name,salary):
        self.name = name
        self._salary = salary
    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self, newsalary):
        if newsalary<0:
            print("Are you seriously trying to take salary from the employee instead of paying him/her for the work")
            print(f"Current Salary stays {self._salary}\n")
        elif newsalary==0:
            print("We are a legal firm and do not support Slavery. Pay that employee some salary.")
            print(f"Current Salary stays {self._salary}\n")
        else:
            self._salary = newsalary
            print(f"New Salary set to {self._salary}\n")

e = Employee("John", 34500)


print(f"Current Salary: {e.salary}\n")

e.salary = -60000
e.salary = 0000
e.salary = 50000

