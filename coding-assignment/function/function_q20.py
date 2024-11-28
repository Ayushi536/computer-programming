"""
ques.20 : Transpose a matrix using a loop:
"""
def transpose(matrix):
    transposed = []
    for i in range(len(matrix[0])):
        transposed_row = []
        for row in matrix:
            transposed_row.append(row[i])
        transposed.append(transposed_row)
    return transposed

print(transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
