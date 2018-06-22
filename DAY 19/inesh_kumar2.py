# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 12:30:29 2018

@author: inesh
"""

import pandas as pd
data=pd.read_csv(('/media/inesh/f32962a9-22d0-44de-adc0-8bb316305013/forsk/DAY 19/Auto_mpg.txt'),delim_whitespace=True,names=["mpg", "cylinders", "displacement","horsepower","weight","acceleration", "model year", "origin", "car name"])

print data["car name"][data["mpg"]==max(data["mpg"])]

data1=data.drop('car name',axis=1)

data1["horsepower"][data1["horsepower"] == "?"] = data["horsepower"].mode()[0]

data1.horsepower = data1.horsepower.astype(float)   
features=data1.iloc[:,1:].values
labels=data1.iloc[:,0].values

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
features=sc.fit_transform(features)


from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)

from sklearn.tree import DecisionTreeRegressor
reg=DecisionTreeRegressor(random_state = 0 )
reg.fit(features_train,labels_train)



from sklearn.ensemble import RandomForestRegressor
foReg=RandomForestRegressor(n_estimators=10,random_state=0)
foReg.fit(features_train,labels_train)





import numpy as np
x=np.array([6,215,100.0,2630,22.2,80,3]).reshape(1,-1)
x = sc.transform(x)
reg.predict(x)
foReg.predict(x)

