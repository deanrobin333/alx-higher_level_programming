#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not isinstance(my_list, list):
        return
    length = len(my_list)
    for i in range(length - 1, -1, -1):
        print("{:d}".format(my_list[i]))
