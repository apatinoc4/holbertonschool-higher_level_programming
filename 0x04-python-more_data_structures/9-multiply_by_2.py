#!/usr/bin/python3
def multiply_by_2(my_dict):
    new_dict = {}
    for i, j in my_dict.items():
        new_dict[j] = i * 2
    return new_dict
