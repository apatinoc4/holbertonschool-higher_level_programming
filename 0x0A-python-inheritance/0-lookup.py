#!/usr/bin/python3


def lookup(obj):
    """
    returns the list of available attributes and methods of an object
    @obj: object (can be any type)
    return: list
    """
    return dir(obj)
