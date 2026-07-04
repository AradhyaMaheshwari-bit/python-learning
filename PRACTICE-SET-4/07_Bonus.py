def fib(n):
    if(n==0 or n==1):
        return n
    return fib(n-2) + fib(n-1)
print(fib(6))


print("=======================")


def safe_divide(a, b):
    if b==0:
        return "Cannot divide by zero"
    return a/b
print(safe_divide(6, 2))
print(safe_divide(2,0))


print("=======================")


import my_utils
print(my_utils.is_even(4))
print(my_utils.is_even(3))
