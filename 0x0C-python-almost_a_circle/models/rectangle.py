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
        [print("") for y in range(0, self.__y)]
        for col in range(0, self.__height):
            [print(" ", end="") for x in range(0, self.__x)]
            for row in range(0, self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """ this is the string representation of the rectangle """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """ this function updates the attributes of a rectangle """
        if args and len(args) != 0:
            for i in range(0, len(args)):
                if i == 0:
                    if args[i] is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = args[i]
                elif i == 1:
                    self.width = args[i]
                elif i == 2:
                    self.height = args[i]
                elif i == 3:
                    self.x = args[i]
                elif i == 4:
                    self.y = args[i]
                else:
                    return
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
                else:
                    return

    def to_dictionary(self):
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }
