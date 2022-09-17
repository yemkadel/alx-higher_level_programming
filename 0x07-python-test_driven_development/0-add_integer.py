#!/usr/bin/python3

""" this a add_integer module """


def add_integer(a, b=98):
    """
    This function adds 2 integers

    Raises a TypeError if a or b is neither an int or a float.

    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
