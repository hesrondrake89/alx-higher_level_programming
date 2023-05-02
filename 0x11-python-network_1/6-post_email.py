#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.
Usage: ./6-post_email.py <URL> <email>
  - Displays the body of the response.
"""

import requests
import sys

if name == "main":
email = {'email': sys.argv[2]}
response = requests.post(sys.argv[1], data=email)
print(response.text)
