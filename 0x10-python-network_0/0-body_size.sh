#!/bin/bash
# a Bash script that takes in a URL, sends a request to that URL,
# and displays the size of the body of the response

if [ -z "$1" ]; then
    echo "Usage: $0 URL"
    exit 1
fi

curl -s "$1" | wc -c
