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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ this function prints a dictionary in json format """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ this function writes a json str representation to a file """
        with open("{}.json".format(cls.__name__),
                  "w", encoding="utf-8") as newFile:
            if list_objs is None:
                newFile.write("[]")
            else:
                newList = [obj.to_dictionary() for obj in list_objs]
                newFile.write(Base.to_json_string(newList))
