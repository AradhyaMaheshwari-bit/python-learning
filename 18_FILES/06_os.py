import os

a = os.listdir(
    "18_FILES/DIR"
)  # list all files and sub directories in the mentioned directory
print(a)

current_dir = os.getcwd()  # get current directory
print("Current Directory: ", current_dir)

files = os.listdir(".")  # "." represents current directory
print("Files in current directory: ", files)

print(os.path.exists("18_FILES/DIR"))   # It checks the path in current directory
print(os.path.exists("dir"))           # although this directory exist it is not in current directory but in "current_directory/18_FILES/""
print(os.path.exists("ami"))

# os.mkdir("new")    # Create a new directory
# os.remove("sample.txt")  # removes the file in "."
# os.rmdir("new")      # Removes empty directory if the dir has file it gives error

# Rename file or directory
# os.rename("sample.txt", "abc.txt") # file or dir must be in "."

