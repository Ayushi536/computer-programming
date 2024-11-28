"""
ques.4 :  Merge Dictionaries with Conflicts
Q: Merge two dictionaries, resolving key conflicts by summing the values.
"""
dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"b": 5, "c": 15, "d": 25}
merged_dict = {key: dict1.get(key, 0) + dict2.get(key, 0) for key in set(dict1) | set(dict2)}
print(merged_dict) 
