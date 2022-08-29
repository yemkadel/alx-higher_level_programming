#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        firstChr = "None"
    else:
        firstChr = sentence[0]
    return len(sentence), firstChr
