#!/usr/bin/python3
'''Defines a Rectangle class'''


class Rectangle:
    '''Rectangle class'''

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Attributes:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
        # or `type(self).number_of_instances += 1`

    @property
    def width(self):
        """Get/set the private width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the private height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''Gets the area of a rectangle'''
        return self.width * self.height

    def perimeter(self):
        '''Gets the perimeter of a rectangle'''
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        '''prints rectangle using #'''

        '''returning is better than printing directly,
        so that you can be able to use the returned rectangle object
        '''
        if self.width == 0 or self.height == 0:
            return ""
        rect = []
        for i in range(self.height):
            [rect.append(str(self.print_symbol)) for _ in range(self.width)]
            if i != self.height - 1:
                rect.append("\n")
        return "".join(rect)

    def __repr__(self):
        '''representation of how to create a rectangle'''
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        bigger = rect_2 if rect_2.area() > rect_1.area() else rect_1
        return bigger
