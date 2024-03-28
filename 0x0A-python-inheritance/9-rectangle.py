#!/usr/bin/python3
# 8-rectangle.py
'''Defines a class ``Rectangle`` that inherits from ``7-base_geometry.py``

Attributes:
    width (int): width of the rectangle.
    height (int): height of the rectangle.
'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Class Rectangle'''

    def __init__(self, width, height):
        '''Creates new instance of a rectangle

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        '''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''Calculates area of rectangle

        Returns:
            int: area
        '''
        return self.__width * self.__height

    def __str__(self):
        '''Returns string representation of the rectangle

        Returns:
            str: [Rectangle] <width>/<height>
        '''
        return f"[Rectangle] {self.__width}/{self.__height}"
