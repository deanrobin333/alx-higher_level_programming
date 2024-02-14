#!/usr/bin/python3
from functools import reduce


def uniq_add(my_list=[]):
    sorted_list = sorted(my_list)
    diff_value = sorted_list[0]
    result = 0

    for i in range(1, len(sorted_list)):
        result += diff_value if diff_value != sorted_list[i] else 0
        diff_value = sorted_list[i]

    if sorted_list[-2] != diff_value:
        result += diff_value

    return result
