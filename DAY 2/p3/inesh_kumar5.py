# -*- coding: utf-8 -*-
"""
Created on Mon May 14 12:25:38 2018

@author: inesh
"""



y=list(input("Enter any numbbers:- "))

print sum(y)
y.sort()
y.pop()
y.pop(0)

print sum(y)/len(y)


