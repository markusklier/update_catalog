#!/usr/bin/env python3

from PIL import Image
import os
import glob

images = glob.glob('~/supplier-data/images/*')

def main():
        for infile in images:
            file, ext = os.path.splitext(infile)
            with Image.open(infile) as im:
                im.convert('RGB').resize((600,400)).save(str('~/supplier-data/images/') + '/' + str(os.path.basename(infile)) + '.jpeg')

if __name__ == '__main__':
    main()
