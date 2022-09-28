#!/usr/bin/python3i
""" This module is about json to string. """
import json


def from_json_string(my_str):
    """ This function returns a json representation of a string obj. """
    return json.loads(my_str)
