#!/usr/bin/python3


"""Defines a Square type with size validation"""


class Square:
    """Creates Square type"""

    def __init__(self, size=0):
        """Initializes Square with size"""
        self.__size = size
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
