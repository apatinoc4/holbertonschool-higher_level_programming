#!/usr/bin/python3
"""base.py"""
import json


class Base:
    """
        Base Class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
    
    @staticmethod
    def to_json_string(list_dictionaries):
        return json.dumps(list_dictionaries) if list_dictionaries is not None else "[]"

    @staticmethod
    def from_json_string(json_string):
        return json.loads(json_string) if json_string is not None else []

    @classmethod
    def save_to_file(cls, list_objs):
        with open("{}.json".format(cls.__name__), "w+") as f:
            f.write(cls.to_json_string([cls.to_dictionary(x) for x in list_objs]))

    @classmethod
    def create(cls, **dictionary):
        tmp = cls(1, 1)
        tmp.update(**dictionary)
        return tmp

    @classmethod
    def load_from_file(cls):
        try:
            with open('{}.json'.format(cls.__name__), 'r') as f:
                tmpDict = cls.from_json_string(f.read())
        except IOError:
            return []
        return [cls.create(**x) for x in tmpDict]
