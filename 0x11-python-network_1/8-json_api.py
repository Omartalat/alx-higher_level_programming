#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) >= 2:
        payload = {'q': sys.argv[1]}
    else:
        payload = {'q': ""}
    response = requests.post(url, data=payload)
    try:
        if response.json():
            dict_ = response.json()
            id = dict_.get('id')
            name = dict_.get('name')
            print('[{}] {}'.format(id, name))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON'8)
