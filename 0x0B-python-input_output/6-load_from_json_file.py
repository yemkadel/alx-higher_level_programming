#!/usr/bin/python3
""" This module is on json. """
import json


def load_from_json_file(filename):
    """ this function creates a json obj from a file txt """
    with open(filename, "r", encoding="utf-8") as f:
        return json.loads(f.read())
