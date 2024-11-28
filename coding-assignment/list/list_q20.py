"""
ques.20 : Find the longest increasing subsequence
Question: Write a program to find the longest increasing subsequence in [10, 9, 2, 5, 3, 7, 101, 18].
"""
lst = [10, 9, 2, 5, 3, 7, 101, 18]
n = len(lst)
longest = [1] * n

for i in range(1, n):
    for j in range(i):
        if lst[i] > lst[j]:
            longest[i] = max(longest[i], longest[j] + 1)

print(max(longest))
