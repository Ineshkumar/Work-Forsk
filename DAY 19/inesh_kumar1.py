# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 11:03:07 2018

@author: inesh
"""

import pandas as pd
data=pd.read_csv('/media/inesh/f32962a9-22d0-44de-adc0-8bb316305013/forsk/DAY 19/PastHires.csv')

features=data.iloc[:,0:-1].values
labels=data.iloc[:,-1].values.reshape(-1,1)


from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()

features[:,1]=le.fit_transform(features[:,1])
features[:,3]=le.fit_transform(features[:,3])
features[:,4]=le.fit_transform(features[:,4])
features[:,5]=le.fit_transform(features[:,5])
labels[:,0]=le.fit_transform(labels[:,0])

from sklearn.tree import DecisionTreeRegressor
reg=DecisionTreeRegressor(random_state = 0 )
reg.fit(features,labels)



from sklearn.ensemble import RandomForestRegressor
foReg=RandomForestRegressor(n_estimators=10,random_state=0)
foReg.fit(features,labels)


import numpy as np
x=np.array([10,1,4,0,1,1]).reshape(1,-1)

#x=np.array([10,y,4,BS,y,n])
#y=np.array([10,n,4,MS,n,y])
foReg.predict(x)