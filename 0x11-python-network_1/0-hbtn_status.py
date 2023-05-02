#!/usr/bin/python3
"""
This script fetches 
- the https://alx-intranet.hbtn.io/status URL using the urllib Python package.
- It then reads the content of the response and prints out its type, content, and UTF-8 decoded content.
"""


if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        content = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
