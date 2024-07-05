#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""
import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    data = {
            'email': sys.argv[2]
            }
    response = requests.post(url, data=data)
    print(response.text)
