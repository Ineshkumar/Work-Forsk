# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 12:48:17 2018

@author: inesh
"""
import pandas as pd
data_17=pd.read_csv('/media/inesh/f32962a9-22d0-44de-adc0-8bb316305013/forsk/Weather/june_17.csv') 
data_18=pd.read_csv('/media/inesh/f32962a9-22d0-44de-adc0-8bb316305013/forsk/Weather/june_18.csv') 
data_19=pd.read_csv('/media/inesh/f32962a9-22d0-44de-adc0-8bb316305013/forsk/Weather/june_19.csv') 

frame=[data_17,data_18,data_19]
result=pd.concat(frame)

mean=0
for i in result["Heat Index"]:
    if(i!='-'):
        mean=mean+float(i)
mean=mean/len(result["Heat Index"])
result["Heat Index"]=result["Heat Index"].replace('-',str(mean))

result["Pressure"]=result["Pressure"].replace('-',result["Pressure"].mode()[0])

result["Visibility"]=result["Visibility"].replace('-',result["Visibility"].mode()[0])

result["Wind Speed"]=result["Wind Speed"].replace('Calm',result["Wind Speed"].mode()[0])


result["Heat Index"]=result["Heat Index"].astype('float64')
result["Pressure"]=result["Pressure"].astype('float64')
#result["Dew Point"].astype('float64')
result["Visibility"]=result["Visibility"].astype('float64')
result["Wind Speed"]=result["Wind Speed"].astype('float64')


features=result.iloc[:,3:].values
labels=result.iloc[:,2].values

from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.25,random_state=0)

from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(features_train,labels_train)

labels_test.reshape(1,-1)
score=lr.score(features_test,labels_test)