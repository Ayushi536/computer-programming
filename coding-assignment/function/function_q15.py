"""
ques.15 : Fibonacci sequence using a loop and functions:
"""
def fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)
    return sequence[:n]

print(fibonacci(10))
