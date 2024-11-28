"""
ques.18 :  Count uppercase and lowercase letters
Question: Count uppercase and lowercase letters in "Hello World".
"""
s = "Hello World"
upper_count = 0
lower_count = 0
for char in s:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1
print(upper_count, lower_count) 
