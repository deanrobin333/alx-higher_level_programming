#!/usr/bin/python3
def multiple_returns(sentence):
    new_tuple = tuple(sentence)
    return len(new_tuple), new_tuple[0] if len(new_tuple) != 0 else None
