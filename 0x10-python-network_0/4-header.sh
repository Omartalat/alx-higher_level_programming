#!/bin/bash
# a Bash script that takes in a URL as an argument, sends a GET request.
curl -sX GET "$1" -H "X-School-User-Id:98"
