# String Formatting

# template = "Dear {}, You are awesome. Take this ${} bag"
# a = "John"
# a1 = 10000
# b = "Jack"
# b1 = 1000
# c = "Marie"
# c1 = 300

# print("Dear {}, You are awesome. Take this ${} bag".format(a,a1))
# s1 = template.format(a,a1)
# print(s1)

# # fstring
# print(f"{a} you are awesome and take this ${a1} bag")

# #character encoding
# print(ord('A'))   # gives ascii value
# print(chr(65))    # gives character value of ascii code

# Padding and Alignment
text = "Python"

# f"{variable:alignment width}"
print(f"{text:>10}")  # Right align
# 1234567890
#     Python
# ^^^^
# 4 spaces


print(f"{text:<10}")  # Left align
print(f"{text:^10}")  # Center align
