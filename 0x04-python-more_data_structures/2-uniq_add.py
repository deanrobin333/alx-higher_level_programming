#!/usr/bin/python3
def uniq_add(my_list=[]):
    '''
        Using `set` would have made life easier
        sorted_list = set(my_list) - creates a unique set
    '''
    sorted_list = sorted(my_list)
    if len(sorted_list) == 0:
        return 0
    result = sorted_list[0]

    for i in range(1, len(sorted_list)):
        if sorted_list[i] != sorted_list[i - 1]:
            result += sorted_list[i]

    return result
