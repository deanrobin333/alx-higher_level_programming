#!/usr/bin/python3
'''Defines a square based on square.py'''


class Square:
    '''Represents a square'''

    def __init__(self, size=0):
        '''
        Initializes a square.

        Args:
            size (int): Size of the new square.
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def size(self):
        '''
        Retrieves the size of the square.

        - Property decorators make the method a normal attribute.
        - It allows you to define a method that can be accessed like
          an attribute, allowing you to call it without using parentheses.
        - It's used to define "getter" methods.
        - Access the size attribute through `self.size`.
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''
        Modifies the size of the square.

        - Syntax: `@<attribute_method>.setter`
        - Used in conjunction with @property.
        - Defines a method that will be called when
            setting the value of the property.
        - Allows modification of the private class attribute through the
            `size` method attribute.
        - Enables left-hand assignment.

        Args:
            value (int): New value to update the size.
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''
        Returns the area of the square.

        Must be positioned after the `@setter` property decorator
        because it depends on the `size` attribute being set.
        '''
        return self.__size * self.__size

    def __eq__(self, other):
        """Define the == comparision to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the != comparison to a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the < comparison to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparison to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > comparison to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= compmarison to a Square."""
        return self.area() >= other.area()
