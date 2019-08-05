# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 09:41:23 2019

@author: Mustafa
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#from xor example
X = np.random.uniform(-1,1,1000)
y = np.random.uniform(-1,1,1000)
isxor = np.logical_xor(X>0,y>0)

df = pd.DataFrame({'x1':X,'x2':y,'y':isxor})

df.to_csv('ex_9.csv',index=False)

