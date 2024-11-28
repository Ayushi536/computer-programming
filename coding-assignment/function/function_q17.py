"""
ques.17 : Write a function to count how many words in a list have more than n characters.
"""
def count_long_words(words, n):
    count = 0
    for word in words:
        if len(word) > n:
            count += 1
    return count

print(count_long_words(["apple", "banana", "cherry", "date"], 5))
