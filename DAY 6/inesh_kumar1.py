# -*- coding: utf-8 -*-
"""
Created on Thu May 17 10:55:32 2018

@author: inesh
"""
import string 
a=string.ascii_lowercase
d=0
x=raw_input("enter any string:- ")
x=set(x)
for i in a:
    if(i not in x):
        d=0
    else:
        d=d+1

if(d==26):
    print 'PANGRAM' 
else:
    print 'not a PANGRAM'


