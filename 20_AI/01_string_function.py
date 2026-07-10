# import re

# def slugify(text):
#     # Convert to lowercase (optional)
#     text = text.lower()

#     # Replace one or more non-alphanumeric characters with a dash
#     text = re.sub(r'[^a-z0-9]+', '-', text)

#     # Remove leading/trailing dashes
#     return text.strip('-')

# print(slugify("hey you are good"))
# print(slugify("Hello, World!"))
# print(slugify("Python@3.14 is awesome!!"))
# print(slugify("   Multiple     Spaces   "))


## Without RE
def slugify(text):
    result = ""

    for char in text.lower():
        if char.isalnum():
            result += char
        else:
            if not result.endswith("-"):
                result += "-"

    return result.strip("-")

print(slugify("hey you are good"))
print(slugify("Hello, World!"))
print(slugify("Python@3.14 is awesome!!"))
print(slugify("   Multiple     Spaces   "))
