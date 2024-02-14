#!/usr/bin/python3
def number_keys(a_dictionary):
    if not isinstance(a_dictionary, dict):
        return 0
    numb_keys = 0
    for key in a_dictionary.keys():
        numb_keys += 1
    return numb_keys
