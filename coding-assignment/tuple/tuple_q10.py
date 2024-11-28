"""
ques.10 : Remove duplicates from a tuple
Question: Write a program to remove duplicate elements from the tuple (1, 2, 3, 2, 4, 1, 5).
"""
tpl = (1, 2, 3, 2, 4, 1, 5)
unique_tpl = ()
seen = set()
for item in tpl:
    if item not in seen:
        unique_tpl += (item,)
        seen.add(item)
print(unique_tpl)
