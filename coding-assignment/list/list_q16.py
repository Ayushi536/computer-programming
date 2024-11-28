"""
ques.16 : Create a new list with squares of all elements
Question: Write a program to create a list of squares from [1, 2, 3, 4, 5].
"""
lst = [1, 2, 3, 4, 5]
squares = []
for num in lst:
    squares.append(num ** 2)
print(squares)  
