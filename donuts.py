# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 11:23:44 2019

@author: Mustafa
"""
import numpy as np
import matplotlib.pyplot as plt

n = 300

theta_in = np.random.uniform(0,2*np.pi,n)
noise_in = np.random.uniform(9.5,10.5,n)

x_in = np.cos(theta_in) * noise_in
y_in = np.sin(theta_in) * noise_in

theta_out = np.random.uniform(0,2*np.pi,n)
noise_out = np.random.uniform(19.5,20.5,n)

x_out = np.cos(theta_out) * noise_out
y_out = np.sin(theta_out) * noise_out

plt.plot(x_in,y_in,'o')
plt.plot(x_out,y_out,'o')

plt.xlim(-30,30)
plt.ylim(-30,30)

plt.show()

