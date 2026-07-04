def factorial(n):
    if(n==0 or n==1):
        return 1
    return n * factorial(n-1)

print(factorial(5))


print("=======================")


def sum_of_digits(n):
    # if(n==0):
    #     return 0
    if(n<10):
        return n
    return sum_of_digits(n//10) + n%10
print(sum_of_digits(12340))
