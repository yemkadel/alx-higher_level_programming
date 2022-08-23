#!/usr/bin/python3
def print_last_digit(number):
    i = number
    if i < 0:
        i *= -1
        i = i % 10
    i = i % 10
    print(f"{i}", end="")
    return i
