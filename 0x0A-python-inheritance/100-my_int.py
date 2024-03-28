#!/usr/bin/python3
'''Defines a class ``MyInt`` that inherits fron ``int``'''


class MyInt(int):
    '''Defines MyInt class'''

    def __eq__(self, other):
        '''The method equal

        Args:
            other (int): integer.

        Returns:
            boolean: True or False.
        '''

        return self.real != other

    def __ne__(self, other):
        '''The method not equal

        Args:
            other (int): integer.

        Returns:
            boolean: True or False.
        '''
        return self.real == other
