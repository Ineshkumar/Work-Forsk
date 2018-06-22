# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 13:08:35 2018

@author: inesh
"""

import pandas as pd
data=pd.read_csv('/media/inesh/f32962a9-22d0-44de-adc0-8bb316305013/forsk/DAY 22/deliveryfleet.csv')

features=data.iloc[:,[1,2]].values

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
wcss=[]
for i in range(1,11):
        kmeans=KMeans(n_clusters=i,init='k-means++',random_state=0)
        kmeans.fit(features)
        wcss.append(kmeans.inertia_)
plt.plot(range(1,11),wcss)
plt.title('The Elbow Method')
plt.xlabel('no of cluster')
plt.ylabel('WCSS')
plt.show()


kmeans=KMeans(n_clusters=2,init='k-means++',random_state=0)
y=kmeans.fit_predict(features)
plt.scatter(features[y==0,0],features[y==0,1],s=100,c='red',label='Cluster 1')
plt.scatter(features[y==1,0],features[y==1,1],s=100,c='yellow',label='Cluster 2')
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=300,c='green',label='centroid')
plt.legend()
plt.show()

#4 group
kmeans=KMeans(n_clusters=4,init='k-means++',random_state=0)
y=kmeans.fit_predict(features)
plt.scatter(features[y==0,0],features[y==0,1],s=100,c='red',label='Cluster 1')
plt.scatter(features[y==1,0],features[y==1,1],s=100,c='yellow',label='Cluster 2')
plt.scatter(features[y==2,0],features[y==2,1],s=100,c='blue',label='Cluster 3')
plt.scatter(features[y==3,0],features[y==3,1],s=100,c='black',label='Cluster 4')
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=300,c='green',label='centroid')
plt.legend()
plt.show()
