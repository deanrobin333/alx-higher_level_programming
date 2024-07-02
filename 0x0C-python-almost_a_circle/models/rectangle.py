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
        '''
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
        '''
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
        '''
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
        '''
        self.__y = y
