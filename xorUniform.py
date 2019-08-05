# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 00:41:37 2019

@author: Mustafa
"""

import numpy as np
import matplotlib.pyplot as plt

X = np.random.uniform(-1,1,1000)
y = np.random.uniform(-1,1,1000)

isxor = np.logical_xor(X>0,y>0)

for i in range(len(isxor)):
    if isxor[i] == True:
        plt.scatter(X[i],y[i],c='b',marker=u'x')
    elif isxor[i] == False:
        plt.scatter(X[i],y[i],c='y',marker=u'o')
        
plt.show()