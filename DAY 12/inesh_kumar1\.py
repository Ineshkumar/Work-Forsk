# -*- coding: utf-8 -*-
"""
Created on Fri May 25 11:35:08 2018

@author: inesh
"""

import numpy as np
import matplotlib.pyplot as plt
incomes = np.random.normal(100.0, 20.0, 10000)
print incomes


import matplotlib.pyplot as plt
plt.hist(incomes, 50)
plt.show()


print np.mean(incomes)

print np.median(incomes)


incomes = np.append(incomes, [1000000000])



import matplotlib.pyplot as plt
plt.hist(incomes, 50)
plt.show()


print np.mean(incomes)

print np.median(incomes)

