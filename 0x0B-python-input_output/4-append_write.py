#!/usr/bin/python3


def append_write(filename="", text=""):
    """
    appends a string at the end of a text (UTF-8) file and returns the number
    of characters added
    """
    with open(filename, 'a', encoding='UTF-8') as f:
        f.write(text)
    return len(text)
