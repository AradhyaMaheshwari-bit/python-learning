fruits = ["apple", "banana", "cherry"]
print(fruits)

print(fruits[0])
# print(fruits.index("banana"))

# fruits.insert(fruits.index("banana"), "orange")
# fruits.remove("banana")
# print(fruits)
fruits[1] = "orange"
print(fruits)

print("Length of list: ",len(fruits))


print("======================")


# a = []
# for i in range(1,11):
#     a.append(i)
a = [i for i in range(1,11)]
print(a)
print(a[:3])
print(a[-3:])
