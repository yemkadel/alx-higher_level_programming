#!/usr/bin/python3
""" The module is about io and json """
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    add_item = load_from_json_file("add_item.json")
except FileNotFoundError:
    add_item = []

add_item.extend(sys.argv[1:])
save_to_json_file(add_item, "add_item.json")
