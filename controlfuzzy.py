#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 09:35:33 2020

@author: andres
"""

import numpy as np 
import matplotlib.pyplot as plt
import skfuzzy as fz

U=np.arange(-85,45,0.1)
U_ETN=fz.trapmf(U,[-85, -85, -30, 0])
U_ETZ=fz.trimf(U,[-30,0,30])
U_ETP=fz.trapmf(U,[0,30,45,45])
plt.plot(U,U_ETN,U,U_ETZ,U,U_ETP)
plt.show()

fuzzy_ETN=fz.interp_membership(U,U_ETN,-6.7)
