#!/usr/bin/python3
# 7-add_item.py

'''Adds all arguments to a Python list and saves to a file'''

import json
from sys import argv

save_file = __import__('5-save_to_json_file').save_to_json_file
load_file = __import__('6-load_from_json_file').load_from_json_file

try:
    load_list = load_file('add_item.json')
except (ValueError, FileNotFoundError):
    load_list = []

for item in argv[1:]:
    load_list.append(item)

save_file(load_list, 'add_item.json')
