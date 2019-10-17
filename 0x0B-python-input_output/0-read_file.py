#!/usr/bin/python3


def read_file(filename=""):
    """
    reads a text file (UTF-8) and prints it to stdout
    """
    with open(filename, encoding='UTF-8') as f:
        print(f.read(), end="")
