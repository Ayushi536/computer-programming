"""
ques. 14 : Find the index of all occurrences of a character
Question: Find all indices of "l" in "hello world".
"""
s = "hello world"
indices = []
for i, char in enumerate(s):
    if char == "l":
        indices.append(i)
print(indices)
