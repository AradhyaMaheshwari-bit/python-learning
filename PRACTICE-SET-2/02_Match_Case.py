day = int(input("Enter a day number: "))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednessday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")



print("===================================")


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

