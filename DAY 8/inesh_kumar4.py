# -*- coding: utf-8 -*-
"""
Created on Tue May 22 10:08:55 2018

@author: inesh
"""

e=[]
lst=[]
while True:
    x=raw_input().lower()
    if(x==''):
        break
    lst.append(x)


for i in lst:
    a=i.split("@")[0]
    b=i.split("@")[1]
    if(a.isalnum() or a.isalpha() or "-" in a or "_" in a):
        if(b.split(".")[0].isalnum() or b.split(".")[0].isalpha() and len(b.split(".")[1])<4):
            e.append(i)

