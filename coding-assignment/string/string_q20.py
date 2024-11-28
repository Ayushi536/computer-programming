"""
ques.20 : Count words in a string
Question: Count the number of words in "Python is fun".
"""
s = "Python is fun"
word_count = 0
for word in s.split():
    word_count += 1
print(word_count) 
