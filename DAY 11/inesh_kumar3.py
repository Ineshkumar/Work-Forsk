# -*- coding: utf-8 -*-
"""
Created on Fri May 25 12:05:58 2018

@author: inesh
"""

import numpy as np
import random
data = np.random.randint(5, 15, 40)
counts = np.bincount(data)
print np.argmax(counts)

a=[]
for i in range(40):
    a.append(random.randint(5,15))

from collections import Counter
b=Counter(a)
b.most_common(1)