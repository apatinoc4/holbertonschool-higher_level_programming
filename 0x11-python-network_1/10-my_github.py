#!/usr/bin/python3
""" display id using github credentials """
import requests
import sys

if __name__ == "__main__":
    r = requests.get('https://api.github.com/user',
                     auth=(sys.argv[1], sys.argv[2]))
    d = r.json()
    print(d.get('id'))
