#!/usr/bin/python3
# 5-save_to_json_file.py
'''defines a function `save_to_json_file`'''

import json


def save_to_json_file(my_obj, filename):
    '''writes an Object to a text file, using a JSON representation

    Args:
        my_obj (type) : python object to serialize
        filename (str) : file to write serialized `my_obj`
    '''
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
