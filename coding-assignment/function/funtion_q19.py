"""
ques.19 : Calculate the dot product of two vectors using a loop:
"""
def dot_product(vector1, vector2):
    result = 0
    for i in range(len(vector1)):
        result += vector1[i] * vector2[i]
    return result

print(dot_product([1, 2, 3], [4, 5, 6]))
