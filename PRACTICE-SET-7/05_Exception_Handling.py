class NegativeNumberError(Exception):
    pass

while True:
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        if (a<0 or b<0):
            raise NegativeNumberError("Please enter a positive number only")
        print(a/b)
    except ValueError:
        print("Please enter integer value")
    except ZeroDivisionError:
        print("Division by zero is not possible")
    except NegativeNumberError as e:
        print(e)
