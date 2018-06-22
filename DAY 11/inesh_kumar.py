# -*- coding: utf-8 -*-
"""
Created on Thu May 24 11:40:43 2018

@author: inesh
"""
import pandas as pd

df=pd.read_csv("/media/inesh/f32962a9-22d044de-adc0-8bb316305013/forsk/DAY 11/training_titanic.csv")

print df["Survived"].value_counts()(normalize = True)
print df["Sex"].value_counts()(normalize = True)


df["Survived"][df["Sex"]=='male'].value_counts()
df["Survived"][df["Sex"]=='female'].value_counts()
