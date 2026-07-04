a = {3, 23, 1}
b = {23, 4, 2, 55, 1}

c = a.union(b)          # c = all unique elements of a and b
print(c)

d = a.intersection(b)   # d = all common elements of a and b
print(d)

e = a.difference(b)     # e = elements of a not in b
print(e)

f = b.difference(a)     # f = elements of b not in a
print(f)
