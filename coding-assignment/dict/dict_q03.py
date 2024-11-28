"""
ques.3 :  Find Key with Maximum Value
Q: Find the key with the maximum value in the dictionary:
"""
scores = {"Alice": 90, "Bob": 85, "Charlie": 95}
key_with_max_value = max(scores, key=scores.get)
print(key_with_max_value)  
