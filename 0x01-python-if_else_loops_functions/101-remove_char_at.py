#!/usr/bin/python3

def remove_char_at(str, n):
    if len(str) < n or n < 0:
        return str
    else:
        new_str = ""
        new_str = str[:n]
        new_str += str[n + 1:]
    return new_str
