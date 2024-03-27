#!/usr/bin/python3
'''Defines a class MyList that inherits from List'''


class MyList(list):
    '''class inheriting from list'''

    def print_sorted(self):
        '''Prints a list in ascending order'''
        list_copy = self[:]
        list_copy.sort()
        print(list_copy)
