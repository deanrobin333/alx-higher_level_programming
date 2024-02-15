#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not a_dictionary:
        return a_dictionary
    list_keys = []
    new_dict = dict(a_dictionary)
    for key, val in a_dictionary.items():
        if val == value:
            list_keys.append(key)

    for i in list_keys:
        if i in a_dictionary:
            del a_dictionary[i]

    return (a_dictionary)
