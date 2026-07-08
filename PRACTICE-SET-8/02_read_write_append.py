with open("PRACTICE-SET-8/tasks.txt", "w") as f:
    string = '''\
line1
line1
line1
'''
    f.write(string)
with open("PRACTICE-SET-8/tasks.txt", "a") as f:
    f.write("Task Completed!")
with open("PRACTICE-SET-8/tasks.txt", "r") as f:
    lines = f.readlines()
    print(lines)
