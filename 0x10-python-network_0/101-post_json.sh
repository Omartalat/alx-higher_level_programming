#!/bin/bash
# a Bash script that sends a JSON POST request to a URL
curl -d @"$2" "$1" -H "Content-Type: application/json"
