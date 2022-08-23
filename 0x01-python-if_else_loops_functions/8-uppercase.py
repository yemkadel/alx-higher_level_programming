#!/usr/bin/python3
def uppercase(str):
    for i in str:
        d = ord(i)
        if d >= 97 and d <= 122:
            d = d - 32
        print("{}".format(chr(d)), end="")
    print("")
