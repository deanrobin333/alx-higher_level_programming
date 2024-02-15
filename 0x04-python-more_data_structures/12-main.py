#!/usr/bin/python3
""" Roman to Integer test file
"""
roman_to_int = __import__('12-roman_to_int').roman_to_int

roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

print()
# others
roman_number = "I"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
if type(roman_to_int("I")) is not int:
    print("Doesn't return an integer")

roman_number = "III"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "XXI"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "CXXIV"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = 89
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = None
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "XCIX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXIX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
