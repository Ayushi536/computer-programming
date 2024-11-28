"""
ques.16 : Largest and smallest elements in a list
"""
def find_extremes(lst):
    if not lst:
        return None, None
    largest = smallest = lst[0]
    for num in lst[1:]:
        if num > largest:
            largest = num
        elif num < smallest:
            smallest = num
    return largest, smallest

print(find_extremes([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))
