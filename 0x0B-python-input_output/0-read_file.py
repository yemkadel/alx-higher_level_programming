#!/usr/bin/python3
""" This module has a function. """


def read_file(filename=""):
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
