#!/usr/bin/python3
"""
This script fetches the https://alx-intranet.hbtn.io/status URL using the urllib Python package.
It then reads the content of the response and prints out its type, content, and UTF-8 decoded content.
"""


if name == 'main':
import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    content = response.read()
    print("Response Body:")
    print("\t- Type: {}".format(type(content)))
    print("\t- Content: {}".format(content))
    print("\t- Decoded Content (UTF-8): {}".format(content.decode('utf-8')))
