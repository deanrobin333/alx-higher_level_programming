#!/usr/bin/python3
# 0-read_file.py
'''defines a function tha reads a file'''


def read_file(filename=""):
    '''Reads a file

    Args:
        filename (str, optional) : name of file to read
    '''

    with open(filename, 'r', encoding='utf-8') as f:
        read_file = f.read()
        print(read_file, end="")
