#!/usr/bin/python3
# square.py

'''Class square that inherits from Rectangle
def __init__(self, width, height, x=0, y=0, id=None):
'''

from models.rectangle import Rectangle


class Square(Rectangle):
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
