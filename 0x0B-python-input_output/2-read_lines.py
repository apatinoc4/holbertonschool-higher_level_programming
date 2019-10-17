#!/usr/bin/python3


def read_lines(filename="", nb_lines=0):
    """
    reads n lines of a text file (UTF-8) and prints it to stdout
    """
    lines_read = 0
    with open(filename, encoding='UTF-8') as f:
        for line in f:
            if lines_read < nb_lines or nb_lines <= 0:
                print(line, end="")
                lines_read += 1
