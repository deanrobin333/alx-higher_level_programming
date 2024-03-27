#!/usr/bin/python3
'''Returns a function() lookup'''


def lookup(obj):
    '''Function that returns list of available attributes and methods
    of an object

    Parameters:
        obj (class): object
    '''
    return dir(obj)
