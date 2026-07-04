def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                func(a)
        return wrapper
    return decorator

@repeat(7)
def say_hello(a):
    print(f"Hello {a}")

say_hello("Harry")
'''
It replaces the function say hello with this:
def decorator(func):
    def wrapper(a):
        for i in range(n):
            say_hello(a)
    return wrapper

def wrapper(a):
    for i in range(n):
        say_hello(a)

for i in range(7):
    say_hello("Harry")
'''
