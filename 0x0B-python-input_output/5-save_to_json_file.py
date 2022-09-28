#!/usr/bin/python3
""" This module is on json. """
import json


def save_to_json_file(my_obj, filename):
    """ this function writes an obj to a text file in json """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
