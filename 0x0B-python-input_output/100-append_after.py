#!/usr/bin/python3
# 100-append_after.py
'''Module containing a function def append_after'''


def append_after(filename="", search_string="", new_string=""):
    '''Function that inserts a line of text to a file after each line
    containing a specific string

    Arg:
        filename (str): name of file
        search_string (str, optional): string to search. Defaults to ""
        new_string (str, optional): string to insert after. Defaults to "".
    '''
    with open(filename, mode='r') as f:
        lines = f.readlines()

    with open(filename, mode='w') as f:
        for rec in lines:
            if search_string in rec:
                f.write(rec)
                f.write(new_string)
            else:
                f.write(rec)
