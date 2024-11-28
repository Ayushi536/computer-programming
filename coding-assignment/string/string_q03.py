"""
ques. 3:Replace spaces with underscores
Question: Replace spaces with underscores in "hello world".
"""
s = "hello world"
result = ""
for char in s:
    if char == " ":
        result += "_"
    else:
        result += char
print(result)
