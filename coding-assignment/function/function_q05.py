"""
ques.5 : Define a nested function:
"""
def outer_function():
    def inner_function():
        print("Hello from the inner function!")

    inner_function()

outer_function()
