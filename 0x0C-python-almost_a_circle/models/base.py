#!/usr/bin/python3
# base.py

'''Defines a class Base'''
import json
import os


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
            Base.__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''returns json string representation of "list_dictionaries"

        Args:
            list_dictionaries (list): List of Dictionaries

        Returns:
            (str): json dictionary representation
        '''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''writes the JSON string representation of list_objs to a file

        Args:
            list_objs (list): Instances who inherits of Base - eg
                list of Rectangle or list of Square instances
        '''
        file_name = f"{cls.__name__}.json"  # make output file from class name

        '''List that will hold dictionary representation of all instances
        of each class
        '''
        dic_list = []

        if list_objs:  # if list_objs is not empty
            for i in range(len(list_objs)):  # through every object instance
                '''convert every object instance to it's dictionary
                representation, then append it to the list
                '''
                dic_list.append(list_objs[i].to_dictionary())

        with open(file_name, 'w') as f:
            '''Serialize the dictionary to json string, then write to file'''
            f.write(cls.to_json_string(dic_list))

    @staticmethod
    def from_json_string(json_string):
        '''returns the list of the JSON string representation json_string

        Args:
            json_string (str): json string

        Returns:
            (list): json string representation
        '''
        list_str = []

        if json_string is None or len(json_string) == 0:
            return list_str
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set.

        Args:
            dictionary (dict): double pointer to a dictionary.
            cls (any): class.

        To use the update method to assign all attributes, you must,
        create a “dummy” instance before:
        Create a Rectangle or Square instance with “dummy” mandatory,
        attributes (width, height, size, etc.),
        Call update instance method to this “dummy” instance to apply your,
        real values.
        You must use the method def update(self, *args, **kwargs).
        **dictionary must be used as **kwargs of the method update.
        You are not allowed to use eval.

        Returns:
            list: an instance with all attributes already set.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)

        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances.

        - If the file doesn’t exist, return an empty list.
        - Otherwise, return a list of instances - the type of these instances,
            depends on cls (current class using this method).
        - You must use the from_json_string and create methods.

        Args:
            cls (any): class.

        Returns:
            list: list of instances.
        """
        file_name = f"{cls.__name__}.json"

        if not os.path.exists(file_name):
            return []

        with open(file_name, 'r') as f:
            lst_str = f.read()

        lst_cls = cls.from_json_string(lst_str)

        lst_inst = []

        for i in range(len(lst_cls)):
            lst_inst.append(cls.create(**lst_cls[i]))

        return lst_inst
