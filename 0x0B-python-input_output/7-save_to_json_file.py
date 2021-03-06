#!/usr/bin/python3


import json


def save_to_json_file(my_obj, filename):
    """
    writes the JSON representation of a Python object to a file
    """
    with open(filename, 'w', encoding='UTF-8') as f:
        f.write(json.dumps(my_obj))
