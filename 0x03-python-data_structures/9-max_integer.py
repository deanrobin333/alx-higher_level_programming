#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    max_numb = my_list[0]
    for numb in range(len(my_list)):
        if my_list[numb] > max_numb:
            max_numb = my_list[numb]
    return max_numb
