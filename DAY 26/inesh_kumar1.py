# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 12:35:32 2018

@author: inesh
"""

import pandas as pd
data=pd.read_csv('/media/inesh/f32962a9-22d0-44de-adc0-8bb316305013/forsk/DAY 26/banknotes.csv')

features=data.iloc[:,1:-1].values
labels=data.iloc[:,-1].values


from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.20,random_state=0)

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
classifier.fit(features_train, labels_train)

predi=classifier.predict(features_test)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(labels_test,predi)

score=classifier.score(features_test,labels_test)

from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = classifier, X = features_train, y = labels_train, cv = 10)
print ("mean accuracy is",accuracies.mean())
print (accuracies.std())