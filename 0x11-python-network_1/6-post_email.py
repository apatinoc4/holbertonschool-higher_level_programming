#!/usr/bin/python3
""" post url """
import sys
import requests
if __name__ == "__main__":
    url = sys.argv[1]
    data = {'email': sys.argv[2]}
    html = requests.post(url, data)
    print(html.text)
