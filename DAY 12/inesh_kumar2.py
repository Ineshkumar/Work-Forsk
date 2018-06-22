# -*- coding: utf-8 -*-
"""
Created on Fri May 25 11:57:11 2018

@author: inesh
"""

import numpy as np
import matplotlib.pyplot as plt
data = np.random.normal(150.0, 20.0, 1000)

import matplotlib.pyplot as plt
plt.hist(data, 100)
plt.show()

print data.std()
print data.var()

