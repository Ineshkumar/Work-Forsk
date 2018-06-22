# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 11:01:28 2018

@author: inesh
"""

import pandas as pd
data=pd.read_csv('/media/inesh/f32962a9-22d0-44de-adc0-8bb316305013/forsk/DAY 20/affairs.csv')

data.iloc[-1]=[3,25,3,1,4,16,4,2,0]

features=data.iloc[:,:-1].values


labels=data.iloc[:-1,-1].values.reshape(-1,1)


from sklearn.preprocessing import OneHotEncoder
obj=OneHotEncoder(categorical_features=[-1])
features=obj.fit_transform(features).toarray()

features1=features[:,1:]

from sklearn.preprocessing import OneHotEncoder
obj=OneHotEncoder(categorical_features=[-1])
features1=obj.fit_transform(features1).toarray()

features2=features1[:,1:]

x=features2[-1,:].reshape(1,-1)
features3=features2[:-1,:]

from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features3,labels,test_size=.20,random_state=0)


from sklearn.linear_model import LogisticRegression
lr=LogisticRegression(random_state=0)
lr.fit(features_train,labels_train)


labels_pred=lr.predict(features_test)


from sklearn.metrics import confusion_matrix
cm=confusion_matrix(labels_test,labels_pred)

score=lr.score(features_test,labels_test)

print '%',labels.mean()*100

prediction=lr.predict_proba(x)



import statsmodels.formula.api as sm 
import numpy as np
features3=np.append(arr=np.ones((6365,1)).astype(int),values=features3,axis=1)

features_opt=features3[:,0:]
regressor_ols=sm.OLS(endog=labels,exog=features_opt).fit()
regressor_ols.summary()

features_opt=features3[:,0:16]
regressor_ols=sm.OLS(endog=labels,exog=features_opt).fit()
regressor_ols.summary()




