# -*- coding: utf-8 -*-
"""
Created on Tue May 29 11:08:10 2018

@author: inesh
"""

import pandas as pd
data=pd.read_csv("/media/inesh/f32962a9-22d0-44de-adc0-8bb316305013/forsk/DAY 12/Automobile.csv")

from sklearn.preprocessing import Imputer
imputer=Imputer(missing_values='NaN',strategy='mean',axis=0)
imputer=imputer.fit(data[:,-1])
data[:,-1]=imputer.transform(data[:,-1])