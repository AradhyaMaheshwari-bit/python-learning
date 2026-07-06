def logger(func):
    def wrapper():
        print("Function is being called")
        func()

    return wrapper


@logger
def say_hello():
    print("Hello!")


say_hello()


print("======================")

import time
def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(end-start)
    return wrapper

@timer
def add():
    total = 0
    for i in range(1,1000001):
        total += i
    print(total)

add()
