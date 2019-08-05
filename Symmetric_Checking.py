# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 13:51:16 2019

@author: Mustafa
"""

def check_symmetric(a, tol=1e-8):
    return np.allclose(a,a.T,atol=tol)
