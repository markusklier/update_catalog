#!/usr/bin/env python3

import requests
import glob

url = 'http://localhost/upload/'
images = glob.glob('~/supplier-data/images/*.jpeg')

for image in images:
    with open(image, 'rb') as opened:
        r = requests.post(url, files={'file': opened})
