#!/usr/bin/python3
# 11-student.py

'''Module that defines a class Student'''


class Student:
    '''class that defines properties of a student

    Attributes:
        first_name (str): first name of student
        last_name (str): last name of student
        age (int): age of student
    '''

    def __init__(self, first_name, last_name, age):
        '''instantiates a new student'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Retrieves a dictionary representation of a Student instance.

        If attrs is a list of strings, only attribute names contained in,
        this list must be retrieved.
        Otherwise, all attributes must be retrieved.

        Returns:
            dict: dictionary representation.
        '''
        if attrs is None:
            return vars(self)  # same as 'self.__dict__'

        new_dict = {}

        '''Loop through the strings and if it's a valid key,
        add it to the new dictionary, then return the new_dict'''
        for key in attrs:
            try:
                new_dict[key] = vars(self)[key]
                # same as `self.__dict__[key]`
            except Exception:
                pass
        return new_dict

    def reload_from_json(self, json):
        '''replaces all attributes of the Student instance'''
        try:
            for key, value in self.__dict__.items():
                self.__dict__[key] = json[key]
        except Exception:
            pass
