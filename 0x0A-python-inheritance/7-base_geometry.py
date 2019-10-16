#!/usr/bin/python3


"""
Geometry module:
    classes: BaseGeometry
        methods: area(), integer_validator()
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
