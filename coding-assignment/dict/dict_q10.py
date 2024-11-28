"""
ques.10 : Find Common Keys with Equal Values
Q: Find keys that have the same value in two dictionaries.
"""
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"a": 1, "b": 4, "c": 3, "d": 5}
common_keys = {k: dict1[k] for k in dict1 if k in dict2 and dict1[k] == dict2[k]}
print(common_keys) 
