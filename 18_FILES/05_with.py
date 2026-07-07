# People tend to forget to close the file

f = open("18_FILES/ami.txt", "r")
content = f.read()
print(content)
f.close()


with open("18_FILES/ami.txt", "r") as f:  # context manager
    content = f.read()
    print(content)
    # no need to write f.close() because file is already closed by default even if an error occurs when using with syntax
