"""
ques.8 :  Combine Dictionaries of Lists
Q: Combine two dictionaries, where keys are the same, by merging the lists as values.
"""
dict1 = {"a": [1, 2], "b": [3, 4]}
dict2 = {"a": [5], "b": [6, 7], "c": [8]}

from collections import defaultdict

combined_dict = defaultdict(list)
for d in [dict1, dict2]:
    for k, v in d.items():
        combined_dict[k].extend(v)

result = dict(combined_dict)
print(result)
