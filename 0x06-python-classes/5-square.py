#!/usr/bin/python3


"""Defines a Square type with size validation"""


class Square:
    """
    Creates a Square type
    * methods: area(), my_print()
    * properties/setters: size()
    """

    def __init__(self, size=0):
        """Initializes Square with size"""
        self.size = size

    @property
    def size(self):
        """Returns the size of a Square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets square size if valid"""
        self.__size = value
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """Returns the area of a Square"""
        return self.__size * self.__size

    def my_print(self):
        """Prints a square"""
        rows = 0
        while rows < self.size:
            cols = 0
            while cols < self.size:
                print("#", end="")
                cols += 1
            print()
            rows += 1
        if self.size == 0:
            print()
