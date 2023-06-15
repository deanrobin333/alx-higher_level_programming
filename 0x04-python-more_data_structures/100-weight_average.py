#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)
    numb = 0
    avg = 0
    for i in my_list:
        numb += i[0] * i[1]
        avg += i[1]
    return (numb/avg)
