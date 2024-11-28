"""
ques.6 : Find the largest element in a tuple
Question: Write a program to find the largest number in (10, 20, 5, 40, 15) using a loop.
"""
tpl = (10, 20, 5, 40, 15)
max_num = tpl[0]
for num in tpl:
    if num > max_num:
        max_num = num
print(max_num)
