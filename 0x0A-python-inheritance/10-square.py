#!/usr/bin/python3


"""
Geometry module:
    class: BaseGeometry
        methods: area(), integer_validator()
    class: Rectangle(BaseGeometry)
        attributes: height, width
        methods: __init__, __str__, __repr__
    class: Square(Rectangle)
        attributes: size
        methods: __init__, __str__, __repr__
"""


class BaseGeometry:
    """
    Inherits from `object`
    """
    def area(self):
        """
        Computes and returns the area of a shape
        """
        return self.__size * self.__size

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
        else:
            if name == 'width':
                self.__width = value
            if name == 'height':
                self.__height = value
            if name == 'size':
                self.__size = value


class Rectangle(BaseGeometry):
    """
    Inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        @width: width of rectangle
        @height: height of rectangle
        """
        super().integer_validator('width', width)
        self.__width = width
        super().integer_validator('height', height)
        self.__height = height

    def __repr__(self):
        """
        formal representation of a Rectangle
        """
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)

    def __str__(self):
        """
        informal representation of a Rectangle
        """
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)


class Square(Rectangle):
    """
    Inherits from Rectangle
    """
    def __init__(self, size):
        """
        @size: size of Square
        """
        self.integer_validator('size', size)
        self.__size = size

    def __repr__(self):
        """
        formal representation of a Square
        """
        return '[Rectangle] {}/{}'.format(self.__size, self.__size)

    def __str__(self):
        """
        informal representation of a Square
        """
        return '[Rectangle] {}/{}'.format(self.__size, self.__size)
