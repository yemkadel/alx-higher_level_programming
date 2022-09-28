#!/usr/bin/python3
""" This module is on io. """


def write_file(filename="", text=""):
    """ this function writes to a file. """
    with open(filename, "w", encoding="utf-8") as f:
        return (f.write(text))
