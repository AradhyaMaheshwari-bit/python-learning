while (data := input("Enter data: ")):
    print(data)
    if data == "quit":
        break


words = ["python", "rocks", "ai"]
lengths = [length for word in words if (length := len(word)) >= 4]
print(lengths)
