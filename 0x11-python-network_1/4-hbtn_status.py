#!/usr/bin/python3
""" get pages content """
import requests
if __name__ == "__main__":
    html = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: " + str(type(html.text)))
    print("\t- content: " + html.text)
