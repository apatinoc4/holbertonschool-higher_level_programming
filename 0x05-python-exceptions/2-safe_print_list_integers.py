#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    ints_printed = idx = 0
    while idx < x:
        try:
            if type(my_list[idx]) is int:
                print("{:d}".format(my_list[idx]), end="")
                ints_printed += 1
            idx += 1
        except IndexError:
            raise
    print()
    return ints_printed
