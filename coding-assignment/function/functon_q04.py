"""
ques.4 : Use a function as an argument to another function:
"""
def apply_function(func, value):
    return func(value)

def square(x):
    return x * x

result = apply_function(square, 5)
