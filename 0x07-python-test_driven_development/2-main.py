#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)

matrix = [[3, 7, 9], [5, 9, 11]]
print(matrix_divided(matrix, 3))

matrix = [[1, 2, 3], [4, 5, 6]]
print(matrix_divided(matrix, 3.3))
print(matrix_divided(matrix, -3.3))

matrix = [[3, -2.2, 9], [-6.6, 7.33, 8]]
print(matrix_divided(matrix, 3))

print()
matrix = [[1, 2, 3], [4, 5, 6]]
print(matrix_divided(matrix, 1))

