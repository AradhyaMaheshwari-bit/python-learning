coordinates = (10, 20)

print(coordinates)
print(coordinates[0])
print(coordinates[1])


print("======================")


# coordinates[0] = 50         # tuples are immutable


print("======================")


a = list(coordinates)
print(a)
a[0] = 50
print(a)

a = tuple(a)
print(a)
