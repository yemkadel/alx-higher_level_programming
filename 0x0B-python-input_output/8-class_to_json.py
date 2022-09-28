#!/usr/bin/python3
""" this module defines a python class to json function """


def class_to_json(obj):
    """ this function returns a dict representation of a class """
    return obj.__dict__
