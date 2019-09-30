#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):

    elements_printed = idx = 0
    while elements_printed < x:
        try:
            print(my_list[idx], end="")
            elements_printed += 1
            idx += 1
        except IndexError:
            break
    print()
    return elements_printed
