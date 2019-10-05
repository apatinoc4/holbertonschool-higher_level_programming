#!/usr/bin/python3


"""
add_integer module:
contains a function that adds to integers
"""


def add_integer(a, b):
    """
    adds two integers
    Parameters
    ----------
    a : int or float
    b : int or float
    Returns
    -------
    int
        the sum of a + b
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
        return None
    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')
        return None
    a, b = int(a), int(b)
    return a + b
