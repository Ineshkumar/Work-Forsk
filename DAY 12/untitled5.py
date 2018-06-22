# -*- coding: utf-8 -*-
"""
Created on Fri May 25 10:41:07 2018

@author: inesh
"""

import numpy as np 

x=np.array([[1,2,3],[4,5,6]],np.int32)  #(data ,type of data)
type(x)
x.shape
x.dtype
ndarray -> n direction array



x=np.float32(1.0)

y=np.int_([1,2,3]) #reshape this



z=np.arange(11,dtype=np.uint8)


x=np.array([1,2,3,4])
x=np.array((1,2,3,4))

x=np.zeros((2,3))


x=np.ones((2,3),dtype=np.int8)    pading ->all elements are zero



int np.arange(10)

x=np.linspace(1.,4.,6)

print np.random.random((2,3)


reshape(3,3)

a=[1,2]
b=[3,4]

zip(a,b)

print 10*np.sin(a)


np.mat()



print np.__version__




incomes=np.random.normal(mean,deviation,no og data)


import matplot.pyplot as plt
plt.hist(incomes,50)



income=np.append(incomes,[100000000000000])


#standard deviation    incomes.std()
incomes.var()