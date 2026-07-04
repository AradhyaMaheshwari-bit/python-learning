for i in range(1,11):
    if (i==7):
        break
    print(i)


    print("===================================")


for i in range(1,11):
    if (i==5):
        continue
    print(i)



    print("===================================")


for i in range(1,6):
    match i:
        case 1:
            print(i)
        case 2:
            print(i)
        case 3:
            pass
        case 4:
            print(i)
        case 5:
            print(i)
