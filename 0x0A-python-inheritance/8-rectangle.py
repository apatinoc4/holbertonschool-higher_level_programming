#!/usr/bin/python3


"""
Geometry module:
    class: BaseGeometry
        methods: area(), integer_validator()
    class: Rectangle(BaseGeometry)
        attributes: height, width
"""


class BaseGeometry:
    """
    Inherits from `object`
    """
    def area(self):
        """
        Does nothing, yet
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        @name: string
        @value: integer
        Returns: nothing, just validates value
        """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        elif value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


class Rectangle(BaseGeometry):
    """
    Inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        @width: width of rectangle
        @height: height of rectangle
        """
        self.__width = self.integer_validator('width', width)
        self.__height = self.integer_validator('height', height)
