# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 12:29:58 2018

@author: inesh
"""

import pandas as pd

data=pd.read_csv('/media/inesh/f32962a9-22d0-44de-adc0-8bb316305013/forsk/DAY 17/stats_females.csv')

features=data.iloc[:,1:3].values
labels=data.iloc[:,0].values.reshape(-1,1)

import statsmodels.formula.api as sm


import numpy as np
features=np.append(arr=np.ones((214,1)).astype(int),values=features, axis = 1)

features_opt=features[:,[0,1,2]]
r_OLS=sm.OLS(endog=labels,exog=features_opt).fit()
r_OLS.summary()
r_OLS.params
