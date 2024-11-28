"""
ques.7 : Reverse a tuple using a loop
Question: Write a program to reverse (1, 2, 3, 4, 5) using a loop.
"""
tpl = (1, 2, 3, 4, 5)
reversed_tpl = ()
for i in range(len(tpl) - 1, -1, -1):
    reversed_tpl += (tpl[i],)
print(reversed_tpl)
