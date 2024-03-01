#!/usr/bin/python3
'''Defines a square based on square.py'''


class Square:
    '''Represents a square'''

    def __init__(self, size=0, position=(0, 0)):
        '''
        Initializes a square.

        Args:
            size (int): Size of the new square.
        '''
        '''
        Initialize public attributes,
        which are set based on private attributes.
        This setup allows for value checking during initialization once.
        '''
        self.size = size  # size is defined by `self.__size`
        self.position = position  # position is defined by `self.__position`

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

    @property
    def position(self):
        '''allows to access the `position` attribute through `__position`'''
        return self.__position

    @position.setter
    def position(self, value):
        ''' set the position from a tuple of 2 positive integers'''
        if (
                not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(numb, int) for numb in value) or
                not all(numb >= 0 for numb in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        '''
        Returns the area of the square.

        Must be positioned after the `@setter` property decorator
        because it depends on the `size` attribute being set.
        '''
        return self.__size * self.__size

    def __str__(self):
        '''Prints a square using `#`'''
        if self.size != 0:
            [print() for i in range(self.position[1])]
        for i in range(self.size):
            [print(" ", end="") for k in range(self.position[0])]
            [print("#", end="") for j in range(self.size)]
            ''' if i is 0 '''
            if i != self.size - 1:
                print()

        return ("")
