s = {34, 23, 1, 3, 22}

print(s)

s.add(32)
s.add(322)
s.remove(1)
# s.remove(13242)           # error if not present in set
s.discard(32423)            # if not present in set it will be ignored
s.pop()                     # removes random element

print(s)
