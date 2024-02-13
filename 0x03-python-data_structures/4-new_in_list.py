#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_str = my_list.copy()
    if idx < 0 or idx >= len(new_str):
        return new_str
    new_str[idx] = element
    return new_str
