#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for numb in row:
            print("{:d}".format(numb), end=" " if numb != row[-1] else "")
        print()
