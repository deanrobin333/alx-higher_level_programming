#!/usr/bin/python3
def search_replace(my_list, search, replace):
    replaced_list = my_list.copy()
    for i in range(len(my_list)):
        if my_list[i] == search:
            replaced_list[i] = replace
    return replaced_list
