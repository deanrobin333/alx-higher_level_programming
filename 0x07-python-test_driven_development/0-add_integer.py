#!/usr/bin/python3
'''function that adds integers'''


def add_integer(a, b=98):
    '''
    Converts floating points to integers first, before addition.
    if a or b is not an integer or a float it raises an exception
    '''
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    elif (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    else:
        a = int(a)
        b = int(b)

        return a + b
