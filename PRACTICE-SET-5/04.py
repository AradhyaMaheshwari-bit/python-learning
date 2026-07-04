my_set = {1, 2, 3, 3, 4}
print(my_set)           # only one 3 is printed not two


print("======================")


my_set.add(5)
my_set.remove(2)
print("4 is in the set: ", 4 in my_set)


print("======================")


a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
