#!/usr/bin/python3
# square.py
'''Defines a class Square'''

from models.rectangle import Rectangle


class Square(Rectangle):
    '''class that defines properties of a square
    Inherits properties from Rectangle
    "def __init__(self, width, height, x=0, y=0, id=None):"
    '''
    def __init__(self, size, x=0, y=0, id=None):
        '''creates a square from Rectangle class

        Attr:
            size (int): width and height of square
            x (int, optional): x. Defaults to 0.
            y (int, optional): y. Defaults to 0.
            id (int, optional): Identity of Square. Defaults to 0.
        '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''prints a square
        [Square] (<id>) <x>/<y> - <size> - in our case, width or height
        '''
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        '''property setter for size, determined by width

        Returns:
            (int) : size of one side of square
        '''
        return self.width

    @size.setter
    def size(self, value):
        '''property setter for width of square

        Args:
            value (int): width of square

        Raises:
            TypeError: if width is not an int
            ValueError: if width is less than or equal to 0
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if self.size <= 0:
            raise ValueError("width must be > 0")

        self.width = self.width = value

    def update(self, *args, **kwargs):
        '''assigns attributes

        Args:
            args (int) : arguments
            kwargs (int): key-value based arguments
        '''

        attr = ['id', 'size', 'x', 'y']

        if args is not None and len(args) > 0:
            for i in range(len(args)):
                setattr(self, attr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''returns dictionary representation of a Square

        Returns:
            new_dict : square
        '''
        new_dict = {
            'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y
        }
        return new_dict
