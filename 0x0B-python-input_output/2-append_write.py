#!/usr/bin/python3
""" this module is on io. """


def append_write(filename="", text=""):
    """ this function appends text to a file """
    with open(filename, "a", encoding="utf-8") as f:
        return (f.write(text))
