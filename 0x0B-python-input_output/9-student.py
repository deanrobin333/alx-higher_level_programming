#!/usr/bin/python3
# 9-student.py

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

    def to_json(self):
        return vars(self)  # same as 'self.__dict__'
