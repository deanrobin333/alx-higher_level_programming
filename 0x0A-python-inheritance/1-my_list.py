#!/usr/bin/python3
# 1-my_list.py
'''Defines a class MyList that inherits from List'''


class MyList(list):
    '''class inheriting from list

    Parameter:
        list (list): list to sort
    '''

    def print_sorted(self):
        '''Prints a list in ascending order'''
        list_copy = self[:]
        list_copy.sort()
        print(list_copy)
