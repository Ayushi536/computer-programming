"""
ques.7 : Count Characters in a String
Q: Count the frequency of each character in a string using a dictionary.
"""
text = "programming"
char_count = {}
for char in text:
    char_count[char] = char_count.get(char, 0) + 1
print(char_count) 
