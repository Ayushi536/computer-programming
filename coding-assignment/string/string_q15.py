"""
ques.15 : Remove duplicate characters
Question: Remove duplicate characters from "banana".
"""
s = "banana"
unique_chars = ""
for char in s:
    if char not in unique_chars:
        unique_chars += char
print(unique_chars)
    
