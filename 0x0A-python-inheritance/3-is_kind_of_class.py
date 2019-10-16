#!/usr/bin/python3


def is_kind_of_class(obj, a_class):
    """
    @obj: arbitrary object
    @a_class: arbitrary class
    Returns: True if obj is an instance of a_class, or an instance of a class
    that was inherited from a_class, otherwise False
    """
    return isinstance(obj, a_class)
