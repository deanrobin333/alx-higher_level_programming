#!/usr/bin/python3
# base.py

'''Defines a class Base'''
import json


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

    def to_json_string(list_dictionaries):
        '''returns json string representation of "list_dictionaries"

        Args:
            list_dictionaries (list): List of Dictionaries

        Returns:
            (str): json dictionary representation
        '''

        if list_dictionaries is None or len(list_dictionaries) == "{}"
            return "{}"
        else:
            return json.dumps(list_dictionaries)
