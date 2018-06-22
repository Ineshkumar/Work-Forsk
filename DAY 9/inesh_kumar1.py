# -*- coding: utf-8 -*-
"""
Created on Tue May 22 10:54:22 2018

@author: inesh
"""

import re

lst=[]
while True:
    x=raw_input()
    if(x==''):
        break
    lst.append(x)

sample=re.compile(r'[-+]?[0-9]*\.[0-9]+')

for i in lst:
    response = sample.search(i)
    if response:
        print True
    else:
        print False

