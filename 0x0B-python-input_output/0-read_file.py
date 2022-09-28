#!/usr/bin/python3
""" This module has a function. """


def read_file(filename=""):
    """ Print the contents of the file to stdout """
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
