#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Check if the matrix is not empty and contains lists
    if not matrix or not all(isinstance(row, list) for row in matrix):
        return None

    # Create a new matrix with the squared values of the original matrix
    new_matrix = [[x**2 for x in row] for row in matrix]

    return new_matrix

# Example usage:
original_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

squared_matrix = square_matrix_simple(original_matrix)
print(squared_matrix)  # Output: [[1, 4, 9], [16, 25, 36], [49, 64, 81]]

