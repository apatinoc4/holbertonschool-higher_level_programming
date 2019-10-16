#!/usr/bin/python3


"""
MyList module:
    classes: MyList
    methods: print_sorted()
"""


class MyList(list):
    """
    Inherits from 'list'
    """
    def print_sorted(self):
        """
        Prints a sorted list
        """
        print(sorted(self))
