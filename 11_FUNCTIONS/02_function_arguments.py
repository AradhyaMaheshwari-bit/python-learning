# Positional arguments

# def add(a,b):
#     return a + b

# c = add(3,5)           # values are passed in the position of the parameter and the function is called
# print(c)

# Default Arguments

# def add(a,b, plus=0):
#     return a + b + plus

# c = add(3,5)          #if value not assigned to argument it will take the default parameter
# d = add(3,5,2)
# print(c)
# print(d)

# Keyword Argument

def add(a,b, plus=0):
    return a + b + plus

c = add(3,5,2)
print(c)

c1 = add(b=5, a=3)   #order of argument does not matter
