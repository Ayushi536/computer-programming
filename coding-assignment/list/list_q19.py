"""
ques.19 : Check if a list is a palindrome
Question: Write a program to check if the list [1, 2, 3, 2, 1] is a palindrome.
"""
lst = [1, 2, 3, 2, 1]
is_palindrome = True
for i in range(len(lst) // 2):
    if lst[i] != lst[-(i + 1)]:
        is_palindrome = False
        break
print(is_palindrome)
