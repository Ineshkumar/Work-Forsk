# -*- coding: utf-8 -*-
"""
Created on Tue May 29 10:19:56 2018

@author: inesh
"""


LABEL                no label 
supervised and unsupervised
    |
regration(prediction) values    ->linear 
classfication   yes or no

prediction and no prediction grouping
textual data is categorical data





data=pd.read_csv("/media/inesh/f32962a9-22d0-44de-adc0-8bb316305013/forsk/DAY 13/Cars.csv")
feature=data.iloc[:,1:]
labels=data.iloc[:,0]


imputation--missing value handler by sklearn


from sklearn.preprocessing import imputer
imputer=Imputer(missing_values='NaN',strategy='mean',axis=0) //axis =0 means column wise
imputer.fit(feature[:,1:2])
feature[:,1:2]=imputer.transform(feature[:,1:2])


label encoding convert textual to numeric

from sklearn.preprocessing import LabelEncoder
create obj
feature[]=labelencoder.fit_transform(feature[])

//here problem is priority order

//in the cased of grade we need order

#solution ---->onehotencoding
from sklearn.preprocessing import OneHotEncoder
create obj

feature=onehotencoder.fit_trasform(feature).toarray()



trainig set 






