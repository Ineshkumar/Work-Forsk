# -*- coding: utf-8 -*-
"""
Created on Wed May 16 11:05:04 2018

@author: inesh
"""

import zlib
s='my name is khan'

t=zlib.compress(s)

zlib.decompress(t)

import urllib22

f=urllib2.urlopen("http:......")
f.read(1000)

import os
os.getcwd()


from PIL import image

img_filename=Image.open("sample.jpg")
img_filename.show()


from PIL import ImageFilter
img_filename.filter(ImageFilter.Blur).show()

img_filename.mode