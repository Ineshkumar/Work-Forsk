# -*- coding: utf-8 -*-
"""
Created on Mon May 21 10:51:14 2018

@author: inesh
"""
d=[]
while True:
    x=raw_input()
    if(x==''):
        break
    z=x.split(',')
    d.append((z[0],int(z[1]),int(z[2])))

d.sort()