# -*- coding: utf-8 -*-
"""
Created on Thu May 31 11:36:40 2018

@author: inesh
"""

import pandas as pd

data=pd.read_csv('/media/inesh/f32962a9-22d0-44de-adc0-8bb316305013/forsk/DAY 16/Bahubali2_vs_Dangal.csv')

features=data.iloc[:,0:1].values
labels_b=data.iloc[:,-2].values
labels_d=data.iloc[:,-1].values


from sklearn.linear_model import LinearRegression
#
from sklearn.model_selection import train_test_split
features_train,features_test,labels_b_train,labels_b_test=train_test_split(features,labels_b,test_size=0.2,random_state=0)

#predictions for Bahubali
lr=LinearRegression()
lr.fit(features_train,labels_b_train)
score1=lr.score(features_test,labels_b_test)
print lr.predict(10)

#prediction for dangle
features_train_d,features_test_d,labels_d_train,labels_d_test=train_test_split(features,labels_d,test_size=0.2,random_state=0)
lr2=LinearRegression()
lr2.fit(features_train_d, labels_d_train)
score2=lr2.score(features_test_d,labels_d_test)
print lr2.predict(10)


