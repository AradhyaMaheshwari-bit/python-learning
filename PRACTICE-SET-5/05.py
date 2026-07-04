student = {"name": "John", "age": 20, "grade": "A"}

print(student["name"])
student["grade"] = "A+"
student["city"] = "Delhi"
print(student)


print("======================")


pdict = {"John": 123,
         "Michael": 456,
         "Lily": 789
         }
print(pdict.keys())
print(pdict.values())
print(pdict.items())

for key, value in pdict.items():
    print(f"{key:<8}: {value}")
