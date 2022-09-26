#!/usr/bin/python3
""" The Module defines a sorted list """


class MyList(list):
    """ This is a class that describes a MyList Obj """

    def print_sorted(self):
        """ The function returns a sorted list """
        print(sorted(self))
