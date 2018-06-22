# -*- coding: utf-8 -*-
"""
Created on Mon May 21 11:48:26 2018

@author: inesh
"""

from collections import OrderedDict

d=OrderedDict()
t=''
q=0
while True:
    x=raw_input()
    if(x==''):
        break
    z=x.split(' ')
    for i in z:
        if(i.isalpha()):
            t=t+i+' '
        else:
            q=i
    if t in d:
        d[t] = d[t]+int(q)
    else:
        d[t]=int(q)
    
    t=''
    q=0
for i in d:
    print i, d[i]