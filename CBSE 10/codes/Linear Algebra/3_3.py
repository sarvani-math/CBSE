# -*- coding: utf-8 -*-
"""3.2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GvuGl_svfgTfgLcmydFs9PfnODPn8p54
"""

import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
from numpy import linalg as LA
import sys 
import sympy as sym

r = 2.5
h = 10

v_app = np.pi * (r**2)* h

v_hem = (2/3) * np.pi * (r**3)

v_acc = v_app - v_hem

print(v_acc)

