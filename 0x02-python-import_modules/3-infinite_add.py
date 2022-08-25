#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argLen = len(sys.argv)
    sum = 0
    for i in range(1, argLen):
        sum += int(sys.argv[i])
    print(sum)
