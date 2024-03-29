#!/usr/bin/python3
'''Defines a matrix division function.'''


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix.

    Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor.
    Raises:
        TypeError: If matrix is not a list of list, or if its empty
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        ZeroDivisionError: If div is 0.
        TypeError: If div is not an int or float.
    Returns:
        A new matrix representing the result of the division.
    """
    if (
        not isinstance(matrix, list) or
        matrix == [] or
        not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(ele, int) or isinstance(ele, float)
                for ele in [numb for row in matrix for numb in row])
    ):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
        )

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    elif not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
