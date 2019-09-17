#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        position = None
    else:
        position = sentence[0]
    return (length, position)
