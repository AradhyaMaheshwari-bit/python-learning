age=23 #integer
name="Aradhya" #string
cgpa=8.5 #float

#Rules of defining variables in python
#1. Variable names can only contain letters, numbers, and underscores.
#2. Variable names cannot start with a number.
#3. Variable names are case-sensitive.
#4. Variable names should be descriptive and meaningful.
#5. Avoid using Python reserved keywords as variable names.

# 34age=4   invalid variable name because it starts with a number
age34=4 #valid variable name because it starts with a letter
# a@ge=4 #invalid variable name because it contains a special character
__age = 35 #valid variable name because it starts with two underscores
a_g_e= 36 #valid variable name because it contains only letters and underscores

print(age)
print(name)
print(cgpa)

is_adult=True #boolean can also be written as 1 or 0 i.e. True=1 and False=0
print(is_adult)

print(type(age))
print(type(name))
print(type(cgpa))
print(type(is_adult))