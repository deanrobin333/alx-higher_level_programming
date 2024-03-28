#!/usr/bin/python3
# 7-base_geometry.py
'''Defines a class BaseGeometry based on 6-base_geometry.py'''


class BaseGeometry:
    '''Class BaseGeometry'''

    def area(self):
        '''Area function.

        Raises:
            Exception: "area is not implemented."
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''Validates value

        Args:
            name (str): name of the object.
            value (int): value of the property.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than or equal to 0.

        '''
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
