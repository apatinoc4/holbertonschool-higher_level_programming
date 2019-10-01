#!/usr/bin/python3


"""Defines a Square type with size validation"""


class Square:
    """
    Creates a Square type
    * methods: area(), my_print()
    * properties/setters: size()
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes Square with size"""
        self.size = size
        try:
            self.position = position
        except TypeError as err:
            print(err)

    @property
    def position(self):
        """Returns the position of a Square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets Square position if valid"""
        if type(value) is not tuple or \
            len(value) != 2 or \
            type(value[0]) is not int or type(value[1]) is not int or \
                value[0] < 0 or value[1] < 0:
                    self.__position = None
                    raise TypeError(
                            "position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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
        """Prints a square in position"""
        if self.position:
            if self.size > 0:
                print("\n" * self.position[1], end="")
                row = 0
                while row < self.size:
                    print(" " * self.position[0], end="")
                    print("#" * self.size)
                    row += 1
            elif self.size == 0:
                print()
