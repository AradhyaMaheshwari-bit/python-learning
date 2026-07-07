try:
    f = open("18_FILES/ami.txt", "r")  # rt = text file [Default] , rb = binary files

    for line in f:    # efficient for large files
        print(line)

    f.close()
except FileNotFoundError:
    print("File not found.")

