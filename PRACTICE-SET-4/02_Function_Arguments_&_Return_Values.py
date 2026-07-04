def full_name(first, last):
    # name = first + " " + last
    name = f"{first} {last}"
    return name

print(full_name("First", "Last"))

# first = input("Enter your first name: ")
# last = input("Enter your last name: ")
# print(full_name(first, last))


print("=======================")


def calculate_area(length, width=10):
    return length*width
print(f"Area of this rectangle is: {calculate_area(6,7)}")
print(f"Area of this rectangle is: {calculate_area(8)}")
