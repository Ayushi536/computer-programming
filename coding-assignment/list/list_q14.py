"""
ques.14 :  Find Maximum Element
Write a program to find the maximum element of a list using a for loop.
"""
numbers = [12, 45, 7, 23, 56, 89, 34]
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print(max_num)
