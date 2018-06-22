# -*- coding: utf-8 -*-
"""
Created on Thu May 24 12:39:45 2018

@author: inesh
"""

import pandas as pd

df=pd.read_csv("/media/inesh/f32962a9-22d0-44de-adc0-8bb316305013/forsk/DAY 11/training_titanic.csv")

df["Child"]=0


for i in range(df["PassengerId"].count()):
    if(df["Age"][i]>18):
        df["Child"][i]=1
        
df["Child"][df["Age"]<18]=1



        
df["Child"].value_counts(normalize = True)

