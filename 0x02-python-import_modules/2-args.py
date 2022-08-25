#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argLen = len(sys.argv)
    if argLen == 1:
        print("0 arguments.")
    else:
        print("{} arguments:".format(argLen - 1))
        for i in range(1, argLen):
            print("{}: {}".format(i, sys.argv[i]))
