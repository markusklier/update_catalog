!#/usr/bin/#!/usr/bin/env python3

import os
import requests
import json

url = 'http://{}/fruits'.format(os.environ.get('USER')
description_files = '/supplier-data/descriptions/'

for file in description_files:
    with open(file) as f:
        items = [i.strip() for i in f.readlines()]
        image_name = os.path.basename(file).replace('.txt', '.jpeg')
        print('Reading and sending fruit descriptions to server: ' + os.path.basename(file))
        fruits_content = {'name': items[0], 'weight': items[1].replace(' lbs', ''), 'description': items[2], 'image_name': image_name}
        response = requests.post(url, json=fruits_content)
        response.raise_for_status()
