# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 11:23:55 2018

@author: inesh
"""

import pandas as pd

data=pd.read_csv('/media/inesh/f32962a9-22d0-44de-adc0-8bb316305013/forsk/DAY 18/bluegills.csv')

features=data.iloc[:,0].values.reshape(-1,1)
labels=data.iloc[:,1].values.reshape(-1,1)

from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(features,labels)

import matplotlib.pyplot as plt
plt.scatter(features,labels,color='RED')
plt.plot(features,lr.predict(features),color='GREEN')
plt.title('bluegills')
plt.xlabel('age')
plt.ylabel('length')
plt.show()




from sklearn.preprocessing import PolynomialFeatures
poln_obj=PolynomialFeatures(degree=6)
features_plon=poln_obj.fit_transform(features)


lr1=LinearRegression()
lr1.fit(features_plon,labels)

import matplotlib.pyplot as plt
plt.scatter(features,labels,color='RED')
plt.plot(features,lr1.predict(features_plon),color='GREEN')
plt.title('bluegills')
plt.xlabel('age')
plt.ylabel('length')
plt.show()

import numpy as np
features_grid=np.arange(min(features),max(features),0.1)
features_grid=features_grid.reshape((-1,1))
plt.scatter(features,labels,color='RED')
plt.plot(features_grid,lr1.predict(poln_obj.fit_transform(features_grid)),color='GREEN')
plt.title('bluegills')
plt.xlabel('age')
plt.ylabel('length')
plt.show()


