# -*- coding: utf-8 -*-
"""
Created on Tue May 22 13:22:14 2018

@author: inesh
"""
import re

lst=[]
while True:
    x=raw_input()
    if(x==''):
        break
    lst.append(x)

sample=re.compile(r'[a-zA-Z0-9-_]+\@[a-zA-Z0-9]+\.[a-zA-z]{2,4}')

for i in lst:
    response = sample.match(i)
    if response:
        print 'Valid'
    else:
        print 'Invalid'

