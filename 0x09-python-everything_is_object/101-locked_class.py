#!/usr/bin/python3
""" this is LockedClass module """


class LockedClass:
    """
    This class prevents users from instantiating a LockedClass
    attributes unless called 'first_name'
    """
    __slots__ = ["first_name"]
