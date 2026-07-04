text = input("Enter a Sentence: ")

vowels = ['a','e','i','o','u']
sum = 0

for char in text.lower():
    if (char in vowels):
        sum += 1
print(f"There are {sum} vowels in this sentence.")

string = input("Enter a word: ")
if (string==string[::-1]):
    print("This word is a Palindrome")
else:
    print("This word is not a Palindrome")
