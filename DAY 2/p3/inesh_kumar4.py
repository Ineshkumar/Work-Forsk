# -*- coding: utf-8 -*-
"""
Created on Mon May 14 12:09:15 2018

@author: inesh
"""

x = raw_input("enter the string :- ") 
j,k=0,0

for i in x:
    if(i.isdigit()):
        j=j+1
    elif(i.isalpha()):
        k=k+1
        
print 'digit',j
print 'alpha',k    
    