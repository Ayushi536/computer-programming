"""
ques.5 : Invert a Dictionary
Q: Invert the keys and values of a dictionary, ensuring the values are unique.
"""
data = {"a": 1, "b": 2, "c": 3}
inverted_dict = {v: k for k, v in data.items()}
print(inverted_dict) 
