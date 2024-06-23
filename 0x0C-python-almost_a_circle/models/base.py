#!/usr/bin/python3
# base.py

'''Defines a class Base'''


class Base:
    '''Class that defines the properties of Base

    Attr:
        id (int): Identity of each instance
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Creates an instance of a base

        Attr:
            id (int, optional): Identity of each instance. Defaults to None
        '''
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
