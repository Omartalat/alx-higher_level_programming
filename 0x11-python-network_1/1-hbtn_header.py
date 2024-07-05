#!/usr/bin/python3
"""
a Python script that takes in a URL, and displays the value of X-Request-Id.
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.getheader('X-Request-Id'))
