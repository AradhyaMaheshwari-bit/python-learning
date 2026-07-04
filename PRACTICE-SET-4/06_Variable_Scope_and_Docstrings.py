def increment():
    counter = 0
    counter += 1
    print(counter)
increment()
increment()
increment()

print("=======================")

counter = 0
def incr():
    global counter
    counter += 1
    print(counter)
incr()
incr()
incr()


print("=======================")


def multiply(a, b):
    '''Multiplies two numbers'''
    return a*b
print(multiply(4, 5))
help(multiply)
