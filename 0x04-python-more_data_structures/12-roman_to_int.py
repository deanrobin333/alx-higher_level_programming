#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    sym = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    results = 0
    sum_r = 0

    for i in range(len(roman_string) - 1):

        if sym[roman_string[i]] < sym[roman_string[i + 1]]:
            sum_r = sym[roman_string[i + 1]] - sym[roman_string[i]]
            results += sum_r
            i += 1
        else:
            results += sym[roman_string[i]]
    if len(roman_string) % 2 != 0:
        if sym[roman_string[len(roman_string) - 2]] >= sym[roman_string[-1]]:
            if len(roman_string) == 1:
                results += sym[roman_string[0]]
            else:
                results += sym[roman_string[-1]]
    if (len(roman_string) % 2 == 0):
        if sym[roman_string[len(roman_string) - 2]] >= sym[roman_string[-1]]:
            results += sym[roman_string[-1]]

    return int(results)
