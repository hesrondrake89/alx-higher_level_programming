#!/usr/bin/python3
"""
This script sends an email address to a specified URL using a POST request.
"""
import requests
import sys

if name == "main":
email = {'email': sys.argv[2]}
response = requests.post(sys.argv[1], data=email)
print(response.text)
