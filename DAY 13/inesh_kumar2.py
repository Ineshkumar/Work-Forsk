# -*- coding: utf-8 -*-
"""
Created on Mon May 28 12:38:24 2018

@author: inesh
"""
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('/media/inesh/f32962a9-22d0-44de-adc0-8bb316305013/forsk/DAY 13/Automobile.csv')


a=data.iloc[:,2]
b=list(set(a))
lst_c=data["make"].value_counts()

val = lst_c.head(10)
names = list(val.index)


explode=[]
        
for i in range(0,10):
    if(max(val)==val[i]):
        explode.append(0.2)
    else:
        explode.append(0)



plt.pie(val,labels=names,explode=explode)
plt.show()
