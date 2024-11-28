"""
ques.9 : Flatten a nested tuple
Question: Write a program to flatten a nested tuple ((1, 2), (3, 4), (5, 6)) into a single tuple.
"""
nested_tpl = ((1, 2), (3, 4), (5, 6))
flattened_tpl = ()
for sub_tpl in nested_tpl:
    flattened_tpl += sub_tpl
print(flattened_tpl)
