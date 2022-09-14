#!/usr/bin/python3

""" magic class """

import math


class MagicClass:
    """this is a circle."""

    def __init__(self, radius=0):
        """
            initialize a circle.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """function will return the area."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """function will return The circumference."""
        return (2 * math.pi * self.__radius)
