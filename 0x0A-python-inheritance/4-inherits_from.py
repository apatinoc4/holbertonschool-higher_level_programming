#!/usr/bin/python3


def inherits_from(obj, a_class):
    """
    @obj: arbitrary object
    @a_class: arbitrary class
    Returns: True if obj is an instance of a class that inherited from a_class
    """
    return isinstance(obj, a_class) and a_class is not type(obj)
