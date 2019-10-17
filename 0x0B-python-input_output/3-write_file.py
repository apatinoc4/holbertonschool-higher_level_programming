#!/usr/bin/python3


def write_file(filename="", text=""):
    """
    writes a string to a text file (UTF-8) and returns the number of characters
    written
    """
    with open(filename, 'w', encoding='UTF-8') as f:
        f.write(text)
    return len(text)
