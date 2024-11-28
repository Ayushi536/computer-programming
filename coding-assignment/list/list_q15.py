"""
ques.15 :  Count Negative Numbers
Write a program to count the number of negative numbers in a list using a for loop.
"""
numbers = [12, -45, 7, -23, 56, -89, 34]
count = 0
for num in numbers:
    if num < 0:
        count += 1
print(count)
