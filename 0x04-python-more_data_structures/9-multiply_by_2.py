#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    updated_dict = a_dictionary.copy()
    list_keys = a_dictionary.keys()
    for i in list_keys:
        updated_dict[i] *= 2
    return (updated_dict)
