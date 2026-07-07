numbers = [1, 2, 3, 4, 5]
cubed_numbers = list(map(lambda x:x**3, numbers))
print(cubed_numbers)

numbers = [10, 11, 12, 13, 14]
even = list(filter(lambda x:x%2==0, numbers))
print(even)

from functools import reduce
numbers = [1, 2, 3, 4]
product = reduce(lambda x,y:x*y, numbers)
print(product)
