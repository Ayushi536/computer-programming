"""
ques.8 : Write a function to count the frequency of each character in a string.
"""
def char_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

print(char_frequency("hello"))