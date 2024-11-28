"""
ques.16 : Find the longest word in a string
Question: Find the longest word in "Python is amazing".
"""
s = "Python is amazing"
longest_word = ""
for word in s.split():
    if len(word) > len(longest_word):
        longest_word = word
print(longest_word)
