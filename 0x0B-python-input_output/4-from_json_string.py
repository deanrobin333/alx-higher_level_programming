#!/usr/bin/python3
# 4-from_json_string.py
'''defines a function `from_json_string`'''

import json


def from_json_string(my_str):
    '''returns an object (Python data structure) represented by a JSON string

    Args:
        my_str (str) : json object (string) to process into python object

    Return:
        (type) : python object
    '''

    return json.loads(my_str)
