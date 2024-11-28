"""
ques.17 : Reverse a list using a loop
Question: Write a program to reverse [1, 2, 3, 4, 5] using a loop.
"""
lst = [1, 2, 3, 4, 5]
reversed_lst = []
for i in range(len(lst) - 1, -1, -1):
    reversed_lst.append(lst[i])
print(reversed_lst)  
