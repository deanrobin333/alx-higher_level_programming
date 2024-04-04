#!/usr/bin/python3
# 3-to_json_string.py
'''defines the function `to_json_string`'''

import json


def to_json_string(my_obj):
    '''returns the JSON representation of an object (string):

    Args:
        my_obj (type) : object to process

    Returns:
        (str) : JSON representation of an object
    '''

    return json.dumps(my_obj)
