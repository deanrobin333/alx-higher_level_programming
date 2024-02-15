#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    dict_list = []

    for key, value in a_dictionary.items():
        dict_list.append([key, value])
    sorted_dict = sorted(dict_list, key=lambda x: x[1])

    return sorted_dict[len(sorted_dict) - 1][0]
