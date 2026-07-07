def logger(func):
    def wrapper(*args, **kwargs):
        print("Functin is being called")
        result = func(*args, **kwargs)
        return result
    return wrapper

@logger
def hello():
    print("Hello!")
@logger
def add(a, b):
    return a + b
@logger
def details(name, age):
    print(name, age)

details(name="Alice", age=25)
hello()
print(add(5, 10))
details(name="Alice", age=25)

print("==================================")

class Vector:
    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        return Vector(self.a + other.a)

    def __str__(self) -> str:
        return str(self.a)


n1 = Vector(123)
n2 = Vector(54)
n3 = n1 + n2
print(f"{n1} + {n2} = {n3}")

print("==================")

import logging

logging.basicConfig(
    filename="error.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class InvalidAgeError(Exception):
    pass


while True:
    choice = input("Enter age (or 'q' to quit): ")
    if choice.lower() == "q":
        break
    try:
        age = int(choice)
        if age < 0:
            raise InvalidAgeError("Age cannot be negative.")
        print(f"Your age is {age}\n")
    except ValueError:
        print("Please enter a valid integer.\n")
        logging.error("User entered a non-integer value.")
    except InvalidAgeError as e:
        print(e, "\n")
        logging.error(e)

