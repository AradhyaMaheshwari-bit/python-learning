with open("PRACTICE-SET-8/notes.txt", "w") as f:
    f.write("Learning Python is fun!")
with open("PRACTICE-SET-8/notes.txt", "r") as f:
    content = f.read()
    print(content)
