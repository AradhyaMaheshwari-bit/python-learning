class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"{self.title} by {self.author}"
    def __len__(self):
        return len(self.title)

b1 = Book("Asoiaf", "J.R. Martin")
b2 = Book("Harry Potter","J.K. Rowling")

print(b1)
print(len(b2))
