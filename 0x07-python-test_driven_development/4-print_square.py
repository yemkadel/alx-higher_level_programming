#!/usr/bin/python3
""" square-printing module"""


def print_square(size):
    """
       function raises TypeError: If size is not an integer.
       and  ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
