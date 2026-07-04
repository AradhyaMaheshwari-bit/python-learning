# sum = lambda x:a+b
# a=3
# b=2
# print(sum)

sum = lambda a,b:a+b
print(sum(3, 5))

print("=======================")


num = [1, 2 , 3, 4, 5]
squared = list(map(lambda x:x**2, num))
print(squared)
