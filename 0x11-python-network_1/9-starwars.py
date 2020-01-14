#!/usr/bin/python3
import sys
import requests
if __name__ == "__main__":
    r = requests.get('https://swapi.co/api/people/?search=' + sys.argv[1])
    try:
        d = r.json()
    except ValueError:
        print("Not a valid JSON")
    print("Number of results: " + str(d.get('count')))
    for i in d.get('results'):
        print(i.get('name'))
