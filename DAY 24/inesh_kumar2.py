# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 11:33:29 2018

@author: inesh
"""

from sklearn.datasets import load_iris
iris = load_iris()
iris=iris.data

from sklearn.decomposition import PCA
pca=PCA(n_components=2)
iris=pca.fit_transform(iris)

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
wcss=[]
for i in range(1,11):
        kmeans=KMeans(n_clusters=i,init='k-means++',random_state=0)
        kmeans.fit(iris)
        wcss.append(kmeans.inertia_)
plt.plot(range(1,11),wcss)
plt.title('The Elbow Method')
plt.xlabel('no of cluster')
plt.ylabel('WCSS')
plt.show()

kmeans=KMeans(n_clusters=3,init='k-means++',random_state=0)
y=kmeans.fit_predict(iris)
plt.scatter(iris[y==0,0],iris[y==0,1],s=100,c='red',label='1')
plt.scatter(iris[y==1,0],iris[y==1,1],s=100,c='yellow',label='2')
plt.scatter(iris[y==2,0],iris[y==2,1],s=100,c='green',label='3')
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=300,c='blue',label='centroid')
plt.legend()
plt.show()