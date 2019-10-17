#!/usr/bin/python3


"""
The 13-student Module:
    Class: Student
        Attributes: first_name, last_name, age
        Methods: to_json(), reload_from_json()
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

    def to_json(self, attrs=None):
        """
        @attrs: attributes
        returns dictionary representation of each instance
        """
        if attrs is None:
            return self.__dict__
        selected_attributes = {}
        for existing_attribute, value in self.__dict__.items():
            for requested_attribute in attrs:
                if requested_attribute is existing_attribute:
                    selected_attributes[existing_attribute] = value
        return selected_attributes

        def reload_from_json(self, json):
            """
            @json: dictionary of attribute names and values
            updates the instance attributes with those in json
            """
            for key, value in json.items():
                self.__dict__[key] = value
