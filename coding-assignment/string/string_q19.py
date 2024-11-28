"""
ques.19 : Extract digits from a string
Question: Extract all digits from "abc123def456".
"""
s = "abc123def456"
digits = ""
for char in s:
    if char.isdigit():
        digits += char
print(digits)
