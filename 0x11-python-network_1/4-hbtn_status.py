#!/usr/bin/python3
# Python script that fetches https://alx-intranet.hbtn.io/status
from requests import get

url = "https://alx-intranet.hbtn.io/status"
r = get(url).text
print('Body response:')
print('\t- type: {}'.format(type(r)))
print('\t- content: {}'.format(r))
