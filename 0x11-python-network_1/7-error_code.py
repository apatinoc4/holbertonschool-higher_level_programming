#!/usr/bin/python3
""" checking for error with requests """
import sys
import requests
if __name__ == "__main__":
    html = requests.get(sys.argv[1])
    if html.status_code >= 400:
        print("Error code: " + str(html.status_code))
    else:
        print(html.text)
