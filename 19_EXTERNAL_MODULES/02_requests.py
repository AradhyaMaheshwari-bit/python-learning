import requests

r = requests.get("https://api.github.com/users/AradhyaMaheshwari-bit")

with open("19_EXTERNAL_MODULES/AradhyaMaheshwari-bit.txt", "w") as f:
    f.write(r.text)
