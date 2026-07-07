# import os

# print("Current Working Directory:", os.getcwd())
# print("Script Location:", os.path.dirname(__file__))

f = open("18_FILES/ami.txt", "r")  # rt = text file [Default] , rb = binary files
content = f.read()
print(content)
f.close()

