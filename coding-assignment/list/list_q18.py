"""
ques.18 : Merge two lists into one without duplicates
Question: Write a program to merge [1, 2, 3] and [3, 4, 5] into one list without duplicates using a loop.
"""
lst1 = [1, 2, 3]
lst2 = [3, 4, 5]
merged = lst1[:]
for num in lst2:
    if num not in merged:
        merged.append(num)
print(merged)
