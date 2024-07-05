#!/usr/bin/python3
"""
Write a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
from urllib.request import Request, urlopen
from urllib.parse import urlencode
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    values = {}
    values['email'] = email

    data = urlencode(values).encode('utf-8')
    req = Request(url, data)
    with urlopen(req) as resp:
        print(resp.read().decode('utf-8'))
