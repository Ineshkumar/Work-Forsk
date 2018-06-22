# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 10:15:50 2018

@author: inesh
"""

import pandas as pd
data=pd.read_csv('/media/inesh/f32962a9-22d0-44de-adc0-8bb316305013/forsk/DAY 23/election_data.csv')

data.columns

x=[]
for i in set(data["Name_of_Candidate"]):
    y=list(set(data["Assembly_no"][data["Name_of_Candidate"]==i]))
    if len(y)>1:
        x.append(i)

z=[]
a=[]    
for i in x:
    y=list(set(data["Constituency_no"][data["Name_of_Candidate"]==i]))
    if(len(y)>1):
        z.append(y)
        a.append(i)
    
b=[]
for i in range(0,len(a)):
    y=list(set(data["Votes"][(data["Name_of_Candidate"]==a[i]) and( data["Constituency_no"]==z[i])]))
    b.append(y)