#!/usr/bin/python3


def class_to_json(obj):
    """
    @obj: an instance of a Class
    returns: the dictionary description with simple data structures for JSON
    serialization of an object
    """
    return obj.__dict__
                         
