# -*- coding: utf-8 -*-
"""
Created on Thu May 31 10:44:40 2018

@author: inesh
"""

import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('/media/inesh/f32962a9-22d0-44de-adc0-8bb316305013/forsk/DAY 16/Foodtruck.csv')
features=data.iloc[:,0:1].values
labels=data.iloc[:,-1].values


from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=.20)


from sklearn.linear_model import LinearRegression

linearRegration=LinearRegression()
linearRegration.fit(features_train,labels_train)

labels_pred=linearRegration.predict(features_test)
labels_pred=labels_pred.reshape(-1,1)

Pro_jaipur=linearRegration.predict(3.073)

score=linearRegration.score(features_test,labels_test)

plt.scatter(features_train,labels_train,color='RED')
plt.plot(features_train,linearRegration.predict(features_train),color='GREEN')
plt.title('Foodchain')
plt.xlabel('Population')
plt.ylabel('profit')
plt.show()

