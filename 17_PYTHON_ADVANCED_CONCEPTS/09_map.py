numbers = [1, 2, 3, 4, 5]

# def square(x):
#     return x**2
# new = list(map(square,numbers))
new = list(map(lambda x:x**2, numbers))
print(new)
