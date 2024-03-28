#!/usr/bin/python3
# 11-square.py

'''Defines a class ``Square``
that inherits from `Rectangle` ``9-rectangle.py)``

Attributes:
    width (int): width of the rectangle.
    height (int): height of the rectangle.
'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    ''' Defines a Square class'''

    def __init__(self, size):
        '''Creates new instances of class Square.

        Args:
            size (int): size of 1 side of square.
        '''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        '''returns string representation of the square

        Returns:
            str: [Square] <width>/<height>
        '''

        return f"[Square] {self.__size}/{self.__size}"
