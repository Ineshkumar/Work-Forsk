# -*- coding: utf-8 -*-
"""
Created on Mon May 14 12:35:59 2018

@author: inesh
"""
x=list(input("enter the numbers:-"))
j=0

for i in range(0,len(x)):
      if(x[i]==13):
          continue
      else:
          if(x[i-1]!=13):
              j=j+x[i]        
print j        