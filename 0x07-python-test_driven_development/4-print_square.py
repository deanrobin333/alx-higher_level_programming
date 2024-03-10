#!/usr/bin/python3
# 4-print_square.py
'''defines a square printing function'''


def print_square(size):
    if (
        not isinstance(size, int) or
        (isinstance(size, float) and size < 0)
    ):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        [print("#", end="") for _ in range(size)]
        print()
