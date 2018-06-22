# -*- coding: utf-8 -*-
"""
Created on Mon May 14 11:51:41 2018

@author: inesh
"""

x = raw_input("enter the string :- ") 
y=set(x)
dict1={}
for i in y:
    dict1[i]=x.count(i)
    
    
    
    