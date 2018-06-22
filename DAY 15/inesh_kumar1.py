# -*- coding: utf-8 -*-
"""
Created on Wed May 30 11:00:08 2018

@author: inesh
"""
import pandas as pd
from sklearn import preprocessing
data=pd.read_csv('https://raw.githubusercontent.com/rasbt/pattern_classification/master/data/wine_data.csv',header=None,usecols=[0,1,2])
data.columns = ['Class label', 'Alcohol','Malic acid']


#sta.

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
data=sc.fit_transform(data)


#min max
x = data.values #returns a numpy array
min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x)
data = pd.DataFrame(x_scaled)