# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 11:37:26 2018

@author: inesh
"""

import pandas as pd
import numpy as np
data=pd.read_csv('/media/inesh/f32962a9-22d0-44de-adc0-8bb316305013/forsk/DAY 17/iq_size.csv')

features=data.iloc[:,1:4].values
labels=data.iloc[:,0].values.reshape(-1,1)

from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)



#from sklearn.linear_model import LinearRegression
#lr=LinearRegression()
#lr.fit(features_train,labels_train)
#
#score=lr.score(features_test,labels_test)
#
#x=np.array([90,70,150]).reshape(1,-1)
#print lr.predict(x)


import statsmodels.formula.api as sm

features=np.append(arr=np.ones((38,1)).astype(int),values=features, axis = 1)

features_opt=features[:,[0,1,2,3]]
r_OLS=sm.OLS(endog=labels,exog=features_opt).fit()
r_OLS.summary()

features_opt=features[:,[0,1,2]]
r_OLS=sm.OLS(endog=labels,exog=features_opt).fit()
r_OLS.summary()

features_opt=features[:,[1,2]]
r_OLS=sm.OLS(endog=labels,exog=features_opt).fit()
r_OLS.summary()

features_opt=features[:,[1]]
r_OLS=sm.OLS(endog=labels,exog=features_opt).fit()
r_OLS.summary()


from sklearn.linear_model import LinearRegression
features_train,features_test,labels_train,labels_test=train_test_split(features_opt,labels,test_size=0.2,random_state=0)

lr2=LinearRegression()
lr2.fit(features_train,labels_train)
score=lr2.score(features_test,labels_test)
x=np.array(90).reshape(1,-1)
print lr2.predict(x)