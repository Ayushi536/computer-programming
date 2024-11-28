"""
ques.8 : Merge two tuples alternately
Question: Write a program to merge two tuples alternately. For example, merge (1, 2, 3) and (4, 5, 6) to get (1, 4, 2, 5, 3, 6).
"""
tpl1 = (1, 2, 3)
tpl2 = (4, 5, 6)
merged_tpl = ()
for i in range(len(tpl1)):
    merged_tpl += (tpl1[i], tpl2[i])
print(merged_tpl)
