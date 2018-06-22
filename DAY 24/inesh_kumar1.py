# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 11:00:51 2018

@author: inesh
"""

import pandas as pd
data=pd.read_csv('/media/inesh/f32962a9-22d0-44de-adc0-8bb316305013/forsk/DAY 24/crime_data.csv')

data1=data.iloc[:,[1,2,4]].values

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
data1=sc.fit_transform(data1)

from sklearn.decomposition import PCA
pca=PCA(n_components=2)
data1=pca.fit_transform(data1)


from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
wcss=[]
for i in range(1,11):
        kmeans=KMeans(n_clusters=i,init='k-means++',random_state=0)
        kmeans.fit(data1)
        wcss.append(kmeans.inertia_)
plt.plot(range(1,11),wcss)
plt.title('The Elbow Method')
plt.xlabel('no of cluster')
plt.ylabel('WCSS')
plt.show()


kmeans=KMeans(n_clusters=4,init='k-means++',random_state=0)
y=kmeans.fit_predict(data1)
plt.scatter(data1[y==0,0],data1[y==0,1],s=100,c='red',label='1')
plt.scatter(data1[y==1,0],data1[y==1,1],s=100,c='yellow',label='2')
plt.scatter(data1[y==2,0],data1[y==2,1],s=100,c='green',label='3')
plt.scatter(data1[y==3,0],data1[y==3,1],s=100,c='blue',label='4')
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=300,c='cyan',label='centroid')
plt.legend()
plt.show()