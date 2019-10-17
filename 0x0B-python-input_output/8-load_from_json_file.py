#!/usr/bin/python3


import json


def load_from_json_file(filename):
    """
    creates a Python object from a JSON file
    """
    with open(filename, encoding='UTF-8') as f:
        return json.load(f)
