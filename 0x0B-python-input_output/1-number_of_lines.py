#!/usr/bin/python3


def number_of_lines(filename=""):
    """
    returns the number of lines in a file
    """
    with open(filename, encoding="UTF-8") as f:
        line_count = 0
        for line in f:
            line_count += 1
        return line_count
