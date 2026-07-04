a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter Operation(+,-,*,/): ")

match op:
    case "+":
        print(a+b)
    case "-":
        print(a-b)
    case "*":
        print(a*b)
    case "/":
        print(a/b)
