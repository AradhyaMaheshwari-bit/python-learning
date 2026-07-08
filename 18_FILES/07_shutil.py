import shutil
import os

# It is advised to use os whenever possible instead of shutil
shutil.rmtree("18_FILES/dir")  # deletes the directory whether it is empty or not

# Programmatically copy a file
# shutil.copy("18_FILES/ami.txt", "18_FILES/John.txt")
# os.remove("18_FILES/Jogn.txt")

os.mkdir("18_FILES/dir")
# Move a file or directory
shutil.move("18_FILES/John.txt", "18_FILES/dir/")
