#!/usr/bin/env python3
# -%- coding: utf-8 -%-

import os
import sys
import requests
import json
from pprint import pprint

API_KEY = os.environ.get('API_KEY')
USER_ID = os.environ.get('USER_ID')
if not API_KEY:
    print("no API_KEY env variable set")
    sys.exit(os.EX_USAGE)
if not USER_ID:
    print("no USER_ID env variable set")
    sys.exit(os.EX_USAGE)

print(sys.argv)
argv_len = len(sys.argv)
if argv_len < 3 or argv_len >= 2 and sys.argv[1] in ['-h', '--help']:
    print("publish.py file title [tags...]")
    sys.exit(0)

[_, path, title, *tags] = sys.argv

headers = {
    "Authorization": "Bearer {api_key}".format(api_key=API_KEY),
    "Content-Type": "application/json; charset=utf-8",
    "Accept": "application/json; charset=utf-8",
}
url = "https://api.medium.com/v1/users/{user_id}/posts".format(user_id=USER_ID)

try:
    with open(path) as fo:
        content = fo.read()
except FileNotFoundError:
    print("File \"{}\" not found.".format(sys.argv[1]))
    sys.exit(os.EX_OSFILE)
data = {
    "title": title,
    "content": content,
    "tags": tags,
    "publishStatus": "public",
}

resp = requests.post(url, headers, data=json.dumps())
if not (200 <= resp.status < 300):
    print("api.medium.com returned with ".format(resp.status_code))
    if resp.headers['content-type'].startswith('application/json'):
        pprint(resp.json())

sys.exit(os.EX_OK if 200 <= resp.status_code < 300 else os.EX_DATAERR)
