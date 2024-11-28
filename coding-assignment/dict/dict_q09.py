"""
ques.9 :  Sort Nested Dictionary by Key
Q: Sort a nested dictionary by keys of the inner dictionaries.
"""
nested_dict = {
    "group1": {"b": 2, "a": 1},
    "group2": {"d": 4, "c": 3}
}
sorted_nested_dict = {k: dict(sorted(v.items())) for k, v in nested_dict.items()}
print(sorted_nested_dict)  
