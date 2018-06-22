# -*- coding: utf-8 -*-
"""
Created on Tue May 29 14:11:04 2018

@author: inesh
"""
import pandas as pd
data=pd.read_csv("/media/inesh/f32962a9-22d0-44de-adc0-8bb316305013/forsk/DAY 14/Loan.csv")
data=data.drop('Loan_ID',axis=1)
features=data.drop("Target",axis=1)
labels=data["Target"]

for i in features:
    if features[i].dtype==object:
        features[i]=features[i].astype('category')
        features[i]=features[i].cat.codes

labels=labels.astype('category')
labels=labels.cat.codes

features = pd.get_dummies(features, columns=["Property_Area"])

features=features.values
labels=labels.values

from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=.20,random_state=0)



