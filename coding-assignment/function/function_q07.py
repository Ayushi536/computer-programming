"""
ques.7 : Write a function to find the sum of all elements in a list.
"""
def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_of_list([1, 2, 3, 4, 5]))
