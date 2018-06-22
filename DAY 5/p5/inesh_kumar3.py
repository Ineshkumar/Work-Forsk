# -*- coding: utf-8 -*-
"""
Created on Wed May 16 11:48:31 2018

@author: inesh
"""

from PIL import Image

t=raw_input("enter the image file name:-")
iobj=Image.open(t)
a=iobj.size[0]/2
b=iobj.size[1]/2
img = iobj.convert('LA').rotate(90).crop((a-80,b-102,a+80,b+102))
img.thumbnail((75,75))
img.save("My Image.png")


iobj.size[0]
iobj.size[1]