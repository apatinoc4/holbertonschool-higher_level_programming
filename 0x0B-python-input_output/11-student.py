#!/usr/bin/python3


"""
The 11-student Module:
    Class: Student
        Attributes: first_name, last_name, age
        Methods: to_json()
"""


class Student():
    """
    Student class:
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialization:
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        returns dictionary representation of each instance
        """
        return self.__dict__
