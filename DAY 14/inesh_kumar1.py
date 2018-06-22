# -*- coding: utf-8 -*-
"""
Created on Tue May 29 12:38:42 2018

@author: inesh
"""

import pandas as pd
old_data=pd.read_csv("/media/inesh/f32962a9-22d0-44de-adc0-8bb316305013/forsk/DAY 14/Automobile.csv")


#print data types of all columns
print old_data.dtypes

new_data=old_data.select_dtypes(exclude=['int64','float64'])


#me
#lst_c=new_data['num_doors'].value_counts()
#val = lst_c.head(1)
#name = list(val.index)
#new_data['num_doors'] = new_data['num_doors'].fillna(name[0])

#bhaiya
new_data['num_doors'] = new_data['num_doors'].fillna(new_data['num_doors'].value_counts().index[0])


new_data["body_style"]=new_data["body_style"].astype('category') 
new_data["body_style"]=new_data["body_style"].cat.codes


new_data = pd.get_dummies(new_data, columns=["drive_wheels"])
new_data = pd.get_dummies(new_data, columns=["body_style"])



