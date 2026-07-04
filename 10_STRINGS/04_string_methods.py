# s = "heLlo WoRld"  # Strings are immutable
# name[0] = "R"   # cannot do this
# a=len(s)  # length of string
# print(a)
# print(s.upper(), s)   # uppercase the entire string
# print(s.lower(), s)   # lowercase the entire string
# print(s.capitalize(), s)  # first letter uppercase
# print(s.title(), s)   # capitalize every word

# s = " \nhello world\n "
# print(s)
# print(s.strip())     # remove starting and ending newlines and spaces
# print(s.lstrip())    # only strips left side
# print(s.rstrip())    # only strips right side

# text = "Python is fun and fun and fun"
# print(text.find("is"))       # give index of first occurance
# print(text.index("is"))      # give index of first occurance
# print(text.replace("fun","awesome"))   #replace all occurance of "fun" with awesome

'''
Both .find() and .index() functions the same but differ in uses as we use .find() if we don't know if the character exist or not, but in .index() we know that the character exist.
'''

text = "Apples,Bananas,Pineapples"

# print(text.split(","))   # convert to list
# print(",".join(['Apples', 'Bananas', 'Pineapples']))    # list to string
# print("".join(['Apples', 'Bananas', 'Pineapples']))

text = "Python123"
print(text.isalpha())   # checks if str has only alphabet
print(text.isdigit())   # checks if str has only digits
print(text.isalnum())   # checks if str has both alphabets and digits
print(text.isspace())   # checks if str has only whitespace characters i.e. Space " " Tab "\t" New line "\n"
