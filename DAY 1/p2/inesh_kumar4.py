# -*- coding: utf-8 -*-
"""
Created on Fri May 11 11:36:16 2018

@author: inesh
"""

str0 = raw_input().strip()

space = str0.find(' ')

print str0[space:].strip(),str0[:space]
