#!/usr/bin/python3
""" letter in url """
import sys
import requests
if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        d = r.json()
        if not bool(d):
            print("No result")
        if bool(d):
            print("[{}] {}".format(d.get('id'), d.get('name')))
    except ValueError:
        print("Not a valid JSON")
