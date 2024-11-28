"""
ques.9 : Write a function to calculate the product of all numbers in a list.
"""
def product_of_list(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

print(product_of_list([1, 2, 3, 4]))
