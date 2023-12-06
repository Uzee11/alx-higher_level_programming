#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same size as the input matrix
    result_matrix = [[x**2 for x in row] for row in matrix]
    return result_matrix

# Example usage:
input_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

output_matrix = square_matrix_simple(input_matrix)
print(output_matrix)
