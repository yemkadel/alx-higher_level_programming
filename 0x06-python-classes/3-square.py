#!/usr/bin/python3

""" This is a Square File """


class Square:
    """ The is a Square class """

    def __init__(self, size=0):
        if (type(size) != int):
            raise TypeError('size must be an integer')
        elif (size < 0):
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """ This method calculates and returns the area
        of a square.
        Fomular is Lenght * breadth
        """
        return self.__size * self.__size
