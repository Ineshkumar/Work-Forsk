# -*- coding: utf-8 -*-
"""
Created on Wed May 16 11:28:10 2018

@author: inesh
"""

def traslate(x):
    ns=''
    for i in x:
        if (i not in ['a','e','i','o','u',' ']):
                ns=ns+i+'o'+i
        else:
            ns=ns+i
    print ns

t=raw_input("enter your string:- ")


traslate(t)