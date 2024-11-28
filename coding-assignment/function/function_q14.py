"""
ques.14 : Use the global keyword in a function:
"""
x = 10

def modify_global():
    global x
    x = 20

modify_global()
print(x)
