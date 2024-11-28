"""
ques.2 : Group Elements by Frequency
Q: Group elements of a list nums = [1, 2, 2, 3, 3, 3, 4] into a dictionary where keys are frequencies and values are lists of numbers with those frequencies.
"""
from collections import defaultdict

nums = [1, 2, 2, 3, 3, 3, 4]
freq_dict = defaultdict(list)
for num in nums:
    freq = nums.count(num)
    freq_dict[freq].append(num)

# Remove duplicates in values
result = {k: list(set(v)) for k, v in freq_dict.items()}
print(result)
