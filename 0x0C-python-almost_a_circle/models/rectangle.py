#!/usr/bin/python3
""" This Module describes a Rectangle model """
from models.base import Base


class Rectangle(Base):
    """ This class defines a Rectangle model """
    @property
    def width(self):
        """ the getter method for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ the setter method for width """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = value

    @property
    def height(self):
        """ the getter method for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ the setter method for height """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = value

    @property
    def x(self):
        """ the getter method for x """
        return self.__x

    @x.setter
    def x(self, value):
        """ the setter method for x """
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @property
    def y(self):
        """ the getter method for y """
        return self.__y

    @y.setter
    def y(self, value):
        """ the setter method for y """
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """ the function returns the area of the rectangle """
        return (self.__width * self.__height)

    def display(self):
        for col in range(0, self.__height):
            for row in range(0, self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """ this is the string representation of the rectangle """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)
