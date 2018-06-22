# -*- coding: utf-8 -*-
"""
Created on Wed May 30 11:35:10 2018

@author: inesh
"""

import pandas as pd

data=pd.read_csv("/media/inesh/f32962a9-22d0-44de-adc0-8bb316305013/forsk/DAY 15/Red_Wine.csv")

features=data.iloc[:,0:-1]
labels=data.iloc[:,-1]

for i in features:
    features[i]=features[i].fillna(features[i].value_counts().index[0])

for i in features:
    if features[i].dtype==object:
        features[i]=features[i].astype('category')
        features[i]=features[i].cat.codes

features = pd.get_dummies(features, columns=["wine names"])

from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=.20,random_state=0)


from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
features_train=sc.fit_transform(features_train)
features_test=sc.transform(features_test)
