#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_int = set(my_list)
    sum = 0
    for i in unique_int:
        sum += i
    return (sum)
