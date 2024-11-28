"""
ques.9 : Count vowels in a string
Question: Count the number of vowels in "hello world".
"""
s = "hello world"
vowels = "aeiou"
count = 0
for char in s:
    if char.lower() in vowels:
        count += 1
print(count)
