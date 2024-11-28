"""
ques.10 : Write a function to generate the first n numbers in the Fibonacci sequence using a loop.
"""
def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

print(fibonacci(10)) 
