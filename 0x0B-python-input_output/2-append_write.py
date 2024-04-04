#!/usr/bin/python3
# 2-append_write.py
'''defines a function ``append_write``'''


def append_write(filename="", text=""):
    '''function that appends a string to a text file
    and returns the number of characters added

    Args:
        filename (str) : name of file
        text (str) : string to append to file

    Returns:
        (int) : number of characters written
    '''

    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
