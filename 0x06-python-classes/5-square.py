#!/usr/bin/python3

""" This is a Square File """


class Square:
    """ The is a Square class """

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """ size getter method """
        return self.__size

    @size.setter
    def size(self, value):
        """ size setter method """
        if (type(value) != int):
            raise TypeError('size must be an integer')
        elif (value < 0):
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """ This method calculates and returns the area
        of a square.
        Fomular is Lenght * breadth
        """
        return self.__size * self.__size

    def my_print(self):
        """ prints special # """
        if self.__size == 0:
            print("")
        else:
            for i in range(0, self.__size):
                for x in range(0, self.__size):
                    print("#", end="")
                    if (x == (self.__size - 1)):
                        print("")
