#!/usr/bin/python3
# rectangle.py

'''Defines Rectangle class'''
from models.base import Base


class Rectangle(Base):
    '''Rectangle class that inherits from Base'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''defines parameters for the Rectangle

        Attributes:
            width (int) : width of rectangle
            height (int) : height of rectangle
            x (int, optional) : x. Defaults to 0
            y (int, optional) : y. Defaults to 0
            id (int, optional) : Identity number of rectangle. Defaults to None
        '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''retrieves the width

        Returns:
            (int) : width of rectangle
        '''
        return self.__width

    @width.setter
    def width(self, width):
        '''property setter for rectangle's width

        Args:
            width (int) : width of rectangle

        Raises
            TypeError: if width is not an integer
            ValueError: if width is less than or equal to 0
        '''
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

    @property
    def height(self):
        '''retrieves the height

        Returns:
            (int) : height of rectangle
        '''
        return self.__height

    @height.setter
    def height(self, height):
        '''property setter for rectangle's height

        Args:
            height (int): height of rectangle

        Raises
            TypeError: if height is not an integer
            ValueError: if height is less than or equal to 0
        '''
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @property
    def x(self):
        '''Retrieves the value of x

        Returns:
            (int): value of x
        '''
        return self.__x

    @x.setter
    def x(self, x):
        '''property setter fo x.

        Args:
            (int): x

        Raises
            TypeError: if x is not an integer
            ValueError: if is less than 0
        '''
        if not isinstance(x, int):
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @property
    def y(self):
        '''Retrieves value of y

        Returns:
            (int) : y
        '''
        return self.__y

    @y.setter
    def y(self, y):
        '''property setter for y

        Args:
            (int): y


        Raises
            TypeError: if y is not an integer
            ValueError: if y is less than 0
        '''
        if not isinstance(y, int):
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    def area(self):
        '''Calculates the area of the rectangle

        Returns
            (int) : area of rectangle
        '''
        return self.__width * self.__height

    def display(self):
        '''prints in stdout Rectangle instance with the character #'''
        [print('#' * self.width) for _ in range(self.height)]

    def __str__(self):
        '''overriding print so that it returns:
        "[Rectangle] (<id>) <x>/<y> - <width>/<height>"
        '''
        return (
                f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
                f"{self.width}/{self.height}"
            )
