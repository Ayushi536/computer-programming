"""
ques.2 : Handle variable-length arguments:
"""
def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

multiply(1, 2, 3, 4)
