#!/usr/bin/python3
def uppercase(str):
    u_str = ""
    for i in str:
        if ord(i) >= ord("a") and ord(i) <= ord("z"):
            u_str += (chr(ord(i) - (ord("a") - ord("A"))))
        else:
            u_str += i
    print("{}".format(u_str))
