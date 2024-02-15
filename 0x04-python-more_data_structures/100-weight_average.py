#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    weight_total = 0
    score_total = 0
    score_list = list(map(lambda x: x[0] * x[1], my_list))

    for i in range(len(my_list)):
        weight_total += my_list[i][1]
    for i in score_list:
        score_total += i

    result = score_total / weight_total

    return result
