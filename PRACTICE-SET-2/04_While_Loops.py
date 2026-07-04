i = 1
sum = 0
while i <= 10:
    print(i)
    sum += i
    i += 1
print("sum: ",sum)


print("===================================")


# password = input("Please enter your password: ")
# while password!="123":
#     print("incorrect password")
#     password = input("Please enter your password: ")
# print("correct password")

entered_password = input("Enter your password: ")
password = "y23eh"
while entered_password != password:
    entered_password = input("Wrong password try again: ")
print("Access Granted")



print("===================================")


num = 123
print(int(str(num)[::-1]))
