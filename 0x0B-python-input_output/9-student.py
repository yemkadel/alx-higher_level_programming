#!/usr/bin/python3
""" This Module defines a student class """


class Student:
    """ This class defines a student """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ this function returns a dict representation of a student """
        return self.__dict__
