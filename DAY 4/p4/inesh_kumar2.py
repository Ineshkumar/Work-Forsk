# -*- coding: utf-8 -*-
"""
Created on Tue May 15 11:45:28 2018

@author: inesh
"""

#1 inch  small 5 inch  big  

x=input("enter the seq:- ")
d=0
for i in range(0,x[0]+1):
    for j in range(0,x[1]+1):
        if(i*1+j*5==x[2]):
            d=1
            break
        else:
            d=0
    if(d==1):
        break

if(d==1):
    print 'true'
else:
    print 'false'

    