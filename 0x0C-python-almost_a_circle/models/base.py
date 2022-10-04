#!/usr/bin/python3
""" This module describes the base class """


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
