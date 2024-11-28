"""
ques.11 : Rotate a list to the right by k steps using a loop:
"""
def rotate_right(lst, k):
    n = len(lst)
    k = k % n
    return lst[-k:] + lst[:-k]

print(rotate_right([1, 2, 3, 4, 5], 2))
