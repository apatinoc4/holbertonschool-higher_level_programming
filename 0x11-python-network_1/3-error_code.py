#!/usr/bin/python3
""" display error code """
import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as html:
            print(html.read().decode())
    except urllib.error.URLError as e:
        print("Error code: " + str(e.code))
