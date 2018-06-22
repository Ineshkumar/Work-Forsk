# -*- coding: utf-8 -*-
"""
Created on Thu May 17 11:27:35 2018

@author: inesh
"""

def reverse(x):
    y=''
    for i in x:
        y=i+y    
    print y
x=raw_input("enter any string:- ")    
reverse(x)