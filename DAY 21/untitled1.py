# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 10:17:46 2018

@author: inesh
"""

#tablue BI
#anlitics vidya 

import pandas as pd

data=pd.read_csv('/media/inesh/f32962a9-22d0-44de-adc0-8bb316305013/forsk/DAY 21/mushrooms.csv')


features=data.iloc[:,[5,-2,-1]].values
labels=data.iloc[:,0].values

from sklearn.preprocessing import LabelEncoder
obj=LabelEncoder()

features[:,0]=obj.fit_transform(features[:,0])
features[:,1]=obj.fit_transform(features[:,1])
features[:,2]=obj.fit_transform(features[:,2])
labels=obj.fit_transform(labels)


from sklearn.preprocessing import OneHotEncoder
objHE=OneHotEncoder(categorical_features=[-1])
features=objHE.fit_transform(features).toarray()

features1=features[:,1:]

from sklearn.preprocessing import OneHotEncoder
objHE=OneHotEncoder(categorical_features=[-1])
features1=objHE.fit_transform(features1).toarray()

features2=features1[:,1:]

from sklearn.preprocessing import OneHotEncoder
objHE=OneHotEncoder(categorical_features=[-1])
features2=objHE.fit_transform(features2).toarray()

features3=features2[:,1:]

from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features3,labels,test_size=0.20,random_state=0)


from sklearn.neighbors import KNeighborsClassifier
objKN=KNeighborsClassifier(n_neighbors=5,p=2)
objKN.fit(features_train,labels_train)

|
score=objKN.score(features_test,labels_test)
print score*100,'%'

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(labels_test,pred)