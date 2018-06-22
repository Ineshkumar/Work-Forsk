# -*- coding: utf-8 -*-
"""
Created on Tue May 29 11:14:10 2018

@author: inesh
"""

import pandas as pd

data=pd.read_csv("/media/inesh/f32962a9-22d0-44de-adc0-8bb316305013/forsk/DAY 14/Loan.csv")

features=data.iloc[:,1:-1].values
labels=data.iloc[:,-1].values


from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder=LabelEncoder()

for i in range(0,6):
    features[:,i]=labelencoder.fit_transform(features[:,i])    

#to view our data of object we convert it into a data frame
view = pd.DataFrame(features)


#on property
#label encoding
features[:,-1]=labelencoder.fit_transform(features[:,-1])

#onehotencoder
onehotencoder=OneHotEncoder(categorical_features=[10])

features=onehotencoder.fit_transform(features).toarray()

#encoder dependent
#features[:,2]=labelencoder.fit_transform(features[:,2])    

from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=.20,random_state=0)