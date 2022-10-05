#!/usr/bin/python3
""" This module describes the base class """
import json


class Base:
    """ This class defines the Base class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ This is the constructor of the base class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ this function prints a dictionary in json format """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
