a = int(input("Enter a number between 1-199: "))
match a :
    case 122:
        print('You won a charger')
    case 3:
        print('you won $5')
    case 6:
        print('You won a camera')
    case _:
        print("Better Luck Next Time")