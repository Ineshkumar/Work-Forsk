# -*- coding: utf-8 -*-
"""
Created on Wed May 16 11:19:50 2018

@author: inesh
"""
for i in range(1,51):
    if(i%15==0):
        print 'FIZZBUZZ'
    elif(i%5==0):
        print 'BUZZ'
    elif(i%3==0):
        print 'FIZZ'
    else:
        print i