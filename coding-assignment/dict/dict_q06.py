"""
ques.6 :  Filter Dictionary by Value
Q: Filter a dictionary to keep only items with values greater than 50.
"""
scores = {"Alice": 45, "Bob": 85, "Charlie": 95, "Dave": 30}
filtered_scores = {k: v for k, v in scores.items() if v > 50}
print(filtered_scores)  
