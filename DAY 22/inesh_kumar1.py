# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 11:55:13 2018

@author: inesh
"""

import pandas as pd

data=pd.read_csv('/media/inesh/f32962a9-22d0-44de-adc0-8bb316305013/forsk/DAY 22/tree_addhealth.csv')

for i in data.columns:
    data[i]=data[i].fillna(data[i].mode()[0])


features=data.iloc[:,[0,6,1,2,3,4,5,8,9,10,11,12,13,14,15]].values
labels=data.iloc[:,7].values

from sklearn.preprocessing import StandardScaler
scalling=StandardScaler()
features=scalling.fit_transform(features)

from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.20,random_state=0)

from sklearn.tree import DecisionTreeClassifier
obj=DecisionTreeClassifier(criterion='entropy',random_state=0)
obj.fit(features_train,labels_train)

score=obj.score(features_test,labels_test)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(labels_test,obj.predict(features_test))


#2nd
features2=data.iloc[:,[0,-9]].values
labels2=data.iloc[:,-4].values


from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features2,labels2,test_size=0.2,random_state=0)

from sklearn.tree import DecisionTreeClassifier
obj=DecisionTreeClassifier(criterion='entropy',random_state=0)
obj.fit(features_train,labels_train)

score=obj.score(features_test,labels_test)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(labels_test,obj.predict(features_test))

#3rd
features3=data.iloc[:,[1,2,3,4,5]].values
labels3=data.iloc[:,7].values

from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features3,labels3,test_size=0.2,random_state=0)

from sklearn.ensemble import RandomForestClassifier
obj=RandomForestClassifier(n_estimators=10,criterion='entropy',random_state=0)
obj.fit(features_train,labels_train)

score=obj.score(features_test,labels_test)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(labels_test,obj.predict(features_test))


