# def sum(a,b):
#     # z, a and b are local variables
#     c = a+b
#     z = 1
#     # it creates a local variable z which is destroyed after this function returns
#     return c
# def great(name):
#     z=32 # local variable
#     print("Hello", name)
# a=9
# b=8
# z=2
# # here z, a and b are global variable
# print(sum(4,6))
# print(a,b)
# print(z)
# print(great("Aradhya"))

x=10 # global

def my_func():
    x = 5 # Local
    print(x)  # output: 5

my_func()
print(x)   # output: 10
