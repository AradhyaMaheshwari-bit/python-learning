# https://regexr.com/

import re
text = "The quick brown fox jumps over the lazy dog. brown"

# search for a pattern returns first occurance
# match = re.search("brown", text)
# print(match)
# if match:
#     print("Match found!")
#     print("Start index: ", match.start())
#     print("End index: ", match.end())

match = re.findall("the", text, re.IGNORECASE)  # Case-insensitive search
print("Matches: ", match)

# Replace all occurrence of a pattern
new_text = re.sub("fox", "cat", text)
print(new_text)
