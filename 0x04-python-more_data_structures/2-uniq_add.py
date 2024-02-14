#!/usr/bin/python3
def uniq_add(my_list=[]):
    sorted_list = sorted(my_list)
    diff_value = sorted_list[0]
    result = sorted_list[0]
    print(sorted_list)

    for i in range(1, len(sorted_list) - 1):
        if diff_value != sorted_list[i - 1]:
            result += diff_value
        diff_value = sorted_list[i + 1]

    if diff_value != sorted_list[len(sorted_list) - 2]:
        result += diff_value
    return result
