#!/usr/bin/python3
""" This is a rectangle module """


class Rectangle:
    """ This class defines a Rectangle """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ constructor for the rectangle class """
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """ getter method for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ the setter method for width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ getter method for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter method for height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if (self.__width == 0 or self.__height == 0):
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """ returns a str representation of the class """
        if (self.__width == 0 or self.__height == 0):
            return ""
        else:
            val = []
            symbol = str(self.print_symbol)
            for x in range(0, self.__height):
                [val.append(symbol) for y in range(0, self.__width)]
                if (x != self.__height - 1):
                    val.append("\n")
            return ("".join(val))

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ del function for the class """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if (rect_1.area() > rect_2.area()):
                return rect_1
            elif (rect_2.area() > rect_1.area()):
                return rect_2
            else:
                return rect_1

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)
