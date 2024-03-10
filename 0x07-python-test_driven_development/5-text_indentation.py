#!/usr/bin/python3
# 5-text_indentation.py
'''Defines a function that prints a text
Attributes:
    text_indentation: prints a text with specific conditions
'''


def text_indentation(text):
    '''Prints a text with 2 new lines after ``.?:``

    Args:
        text (str): string to be printed
    Raises:
        TypeError: if text isn ot of type str
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print(text, end="")
