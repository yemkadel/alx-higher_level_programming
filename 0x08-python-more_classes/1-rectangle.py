#!/usr/bin/python3

""" This is a rectangle module """


class Rectangle:
    """ This class defines a Rectangle """

    def width(self):
        """ getter method for width """
        return self.__width

    def width(self, value):
        """ the setter method for width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def height(self):
        """ getter method for height """
        return self.__height

    def height(self, value):
        """ setter method for height """
        if isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def __init__(self, width=0, height=0):
        """ constructor for the rectangle class """
        self.__width = width
        self.__height = height
