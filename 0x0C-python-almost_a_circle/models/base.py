#!/usr/bin/python3
""" This module describes the base class """
import json
import csv


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

    @staticmethod
    def from_json_string(json_string):
        """ this function returns a iist of JSON STRINGS """
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ this function creates a new instance from a dictionary """
        if dictionary and len(dictionary) != 0:
            if cls.__name__ == "Rectangle":
                new_instance = cls(1, 1)
            else:
                new_instance = cls(1)
            new_instance.update(**dictionary)
            return new_instance

    @classmethod
    def load_from_file(cls):
        """ this function returns a list of instances """
        try:
            with open("{}.json".format(cls.__name__), "r", encoding="utf-8") as clsFile:
                strInstances = clsFile.read()
                newList = [cls.create(**inst) for inst in Base.from_json_string(strInstances)]
                return newList
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ the function writes to CSV file """
        file_name = cls.__name__ + ".csv"
        with open(file_name, "w", newline="") as csv_file:
            if list_objs is None or list_objs == []:
                csv_file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    field_names = ["id", "width", "height", "x", "y"]
                else:
                    field_names = ["id", "size", "x", "y"]
                csv_writer = csv.DictWriter(csv_file, fieldnames=field_names)
                for line in list_objs:
                    csv_writer.writerow(line.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """the function returns list of classes from a csv """
        file_name = cls.__name__ + ".csv"
        try:
            with open(file_name, "r", newline="") as csv_file:
                if cls.__name__ == "Rectangle":
                    field_names = ["id", "width", "height", "x", "y"]
                else:
                    field_names = ["id", "size", "x", "y"]
                new_dicts = csv.DictReader(csv_file, fieldnames=field_names)
                new_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in new_dicts]
                return [cls.create(**d) for d in new_dicts]
        except IOError:
            return []
