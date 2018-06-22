# -*- coding: utf-8 -*-
"""
Created on Mon May 28 13:21:24 2018

@author: inesh
"""
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

data=pd.read_csv("/media/inesh/f32962a9-22d0-44de-adc0-8bb316305013/forsk/DAY 13/Cars.csv")

idep_var=data.iloc[:,1:]
dep_var=data.iloc[:,0]

idep_train,idep_test,dep_train,dep_test=train_test_split(idep_var,dep_var,test_size=0.5,random_state=0)

a=pd.DataFrame(idep_train)
b=pd.DataFrame(idep_test)
c=pd.DataFrame(dep_train)
d=pd.DataFrame(dep_test)


a.to_csv()

a.to_csv('idep_train', sep='\t')
b.to_csv('idep_test', sep='\t')
c.to_csv('dep_train', sep='\t')
d.to_csv('dep_test', sep='\t')