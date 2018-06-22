# -*- coding: utf-8 -*-
"""
Created on Tue May 15 12:53:49 2018

@author: inesh
"""

d=input("enter the key and value:- ")
add=0
for i in d.values():
    if i not in(13,14,17,19):
        add=add+i

print add
        
