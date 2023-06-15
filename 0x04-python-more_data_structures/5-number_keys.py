#!/usr/bin/python3
def number_keys(a_dictionary):
    numb_keys = 0
    list_keys = list(a_dictionary.keys())
    for i in list_keys:
        numb_keys += 1
    return (numb_keys)
