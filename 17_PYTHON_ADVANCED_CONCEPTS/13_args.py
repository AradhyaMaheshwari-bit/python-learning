# def sum(a, b):
#     return a + b
def sum(*args):
    print(args)             # collect the argument values passed to sum and store them in a tuple
    total = 0
    for item in args:
        total += item
    return total

print(sum(1, 2, 7, 10))
