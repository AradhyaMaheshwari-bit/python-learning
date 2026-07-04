def remove_duplicates(numbers):
    return list(set(numbers))

a = [1, 2, 3, 3, 4, 4, 5, 2, 5, 6]
print(remove_duplicates(a))


print("======================")

def highest_product(products):
    return max(products.items(), key= lambda x:x[1])

products = {
    "Laptop": 55000,
    "Phone": 30000,
    "Tablet": 25000,
    "Headphones": 5000
}

product, price = highest_product(products)
print(f"The most expensive product is {product} with price {price}")

# highest_product = ""
# highest_price = 0

# for product in products:
#     if products[product] > highest_price:
#         highest_price = products[product]
#         highest_product = product

# print(highest_product)
# print(highest_price)


print("======================")


products = {
    "Laptop": 55000,
    "Phone": 30000,
    "Tablet": 25000,
    "Headphones": 5000
}
student = {"name": "John", "age": 20, "grade": "A"}

#1
# print(products | student)

#2
def merged_dict(dict1, dict2):
    return {**dict1, **dict2}
print(merged_dict(products, student))

#3
# for key, value in products.items():
#     student[key] = value
# print(student)

#4
# student.update(products)
# print(student)
