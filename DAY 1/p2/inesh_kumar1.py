# -*- coding: utf-8 -*-
"""
Created on Fri May 11 10:54:01 2018

@author: inesh

"""



str0 = """This is a multi line string. This code challenge is to
test your understanding about strings.You need to print some part of this string.
From here print this text without manually counting the indexes."""

#print str0.find('From')
#type (str0.find('From'))


print str0[str0.find('From'):]


