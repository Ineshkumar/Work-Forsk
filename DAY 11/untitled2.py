# -*- coding: utf-8 -*-
"""
Created on Thu May 24 10:36:30 2018

@author: inesh
"""

df=pd.read_csv("")
head
tail
df.dtypes
df.columns
df.axes
df.ndim
size
shape
value

describe()
max()
min()
mean()
median()
std()
sample(10)  #randomly any data

df.head(10).mean()



df['rank'] #access only one column
df.phd

df['salary'].mean()



data frame --->group by

dr_rank=df.groupby(['rank'])

df_rank.mean()




df_sub=df[df['salary']>12000]


df-sub.loc[10:20,['rank']]


df_sub.iloc[10:20,[0,3,4,5]]



salary=pd.read_csv("sa.csv")


salary['phd']=salary['phd'].fillna(salary['phd'].mean())
salary.dropna() #drop a record with  missing vaLUE


salary[['service','salary']].agg['min,''mean','max']


