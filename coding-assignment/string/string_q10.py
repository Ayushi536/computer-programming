"""ques. 10:
Check if a string is a palindrome
Question: Write a function to check if the string "radar" is a palindrome.
"""
s = "radar"
a = s[::-1]
if s == a:
    print("Given string is palindrome") 
else:
    print("Given string is not a palindrome") 
