def very_slow_func():
    print("Something....")
    print("Something....")
    return 70

# if (very_slow_func()>10):               # execute twice due to calling the function twice
#     print(very_slow_func())
# a = very_slow_func()                    # optimize the code to execute only once
# if ((a:=very_slow_func())>10):          # Walrus Operator(:=)
#     print(a)
# else:
#     print("Its not greater than 10")

while (data := input("Enter the value:")):
    print(data)
    if data == "q":
        break
