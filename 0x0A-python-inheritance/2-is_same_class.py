#!/usr/bin/python3


def is_same_class(obj, a_class):
    """
    @obj: arbitrary object
    @a_class: arbitrary class
    Return: True if obj is exactly an instance of a_class, otherwise False
    """
    return issubclass(a_class, type(obj))
