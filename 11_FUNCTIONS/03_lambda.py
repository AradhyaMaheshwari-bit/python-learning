# Syntax:
# lambda arguments: expression

square = lambda x: x*x
'''
As good as writing
def square(x):
    return x*x
'''
sum = lambda x,y: x+y
'''
As good as writing
def sum(x,y):
    return x+y
'''

print(square(3))
print(sum(3, 62))


numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16]

# map(function, iterable)
# map() is a built-in Python function that applies a given function to every element of an iterable and returns a map object.
