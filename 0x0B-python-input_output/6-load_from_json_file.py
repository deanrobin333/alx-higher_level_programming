#!/usr/bin/python3
# 6-load_from_json_file.py
'''Module containing the function `load_from_json_file`'''

import json


def load_from_json_file(filename):
    '''creates an Object from a “JSON file”

    Args:
        filename (str) : JSON file

    Returns:
        (type) : python object
    '''
    # deserialization
    with open(filename, encoding='utf-8') as f:
        return json.load(f)
