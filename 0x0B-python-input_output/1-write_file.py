#!/usr/bin/python3
# 1-write_file.py
'''defines a function ``write_file()``'''


def write_file(filename="", text=""):
    '''function that writes a string to a text file
    and returns the number of characters written

    Args:
        filename (str) : name of file
        text (str) : string to write to file

    Returns:
        (int) : number of characters written
    '''

    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
