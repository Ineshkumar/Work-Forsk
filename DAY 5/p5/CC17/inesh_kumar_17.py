# -*- coding: utf-8 -*-
"""
Created on Wed May 16 11:48:31 2018

@author: inesh
"""

from PIL import Image
img_name = "CC17/sample.jpg"
#t=raw_input("enter the image file name:-")
iobj=Image.open(img_name)
img = iobj.convert('LA').rotate(-90).crop((0,0,160,204))
img.thumbnail((75,75))
img.save("My Image.png")



import os
import zipfile

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

if __name__ == '__main__':
    zipf = zipfile.ZipFile('Python.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir('/media/inesh/f32962a9-22d0-44de-adc0-8bb316305013/forsk/DAY 5/p5/CC17', zipf)
    zipf.close()