def sum_all(*args):
    print(args)
    sum = 0
    for item in args:
        sum += item
    return sum

print(sum_all(1, 2, 7, 10))

def print_details(**kwargs):
    for keys, value in kwargs.items():
        print(f"{keys}:{value}")

print_details(name="Alice", age=25, city="Delhi")
