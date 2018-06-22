# -*- coding: utf-8 -*-
"""
Created on Mon May 21 12:55:45 2018

@author: inesh
"""


x=raw_input()
z=list(x.split())
for i in z:
    if(i>0 and i== i[::-1]):
        d=1
    else:
        d=0
if(d==1):
    print True
else:
    print False
    