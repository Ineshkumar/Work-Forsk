# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 11:17:51 2018

@author: inesh
"""

import pandas as pd
data=pd.read_csv('/media/inesh/f32962a9-22d0-44de-adc0-8bb316305013/forsk/DAY 25/breast_cancer.csv')

data=data.drop("A",axis=1)

for i in data.columns:
    data[i]=data[i].fillna(data[i].mode()[0])

features=data.iloc[:,:-1].values
labels=data.iloc[:,-1].values


from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)

import numpy as np
x=np.array([6,2,5,3,9,4,7,2,2]).reshape(1,-1)

from sklearn.svm import SVC
obj=SVC(kernel='linear',random_state=0)
obj.fit(features_train,labels_train)
score=obj.score(features_test,labels_test)
predict=obj.predict(x)
labels_pred=obj.predict(features_test)

from sklearn.svm import SVC
obj1=SVC(kernel='rbf',random_state=0)
obj1.fit(features_train,labels_train)
score1=obj1.score(features_test,labels_test)
predict1=obj1.predict(x)
labels_pred1=obj.predict(features_test)

from sklearn.svm import SVC
obj2=SVC(kernel='poly',random_state=0)
obj2.fit(features_train,labels_train)
score2=obj2.score(features_test,labels_test)
predict2=obj2.predict(x)
labels_pred2=obj.predict(features_test)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(labels_test,labels_pred)

cm1=confusion_matrix(labels_test,labels_pred1)

cm2=confusion_matrix(labels_test,labels_pred2)