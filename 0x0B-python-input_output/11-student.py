#!/usr/bin/python3
""" This Module defines a student class """


class Student:
    """ This class defines a student """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ this function returns a dict representation of a student """
        if (type(attrs) == list and
                all(type(item) == str for item in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """ sets attributes of student """
        for k, v in json.items():
            setattr(self, k, v)_
