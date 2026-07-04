import math
print(math.sqrt(144))
print(math.sin(math.radians(90)))


print("=======================")


import requests
r = requests.get("https://api.github.com")
print(r.text)
print(r.json())
