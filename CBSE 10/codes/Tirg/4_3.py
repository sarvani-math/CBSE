# -*- coding: utf-8 -*-
"""4.3.ipynb

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

a = math.pi / 6

x = ((math.tan(a)/ (1-math.tan(a)))) - (((1/math.tan(a))/ 1- (1/math.tan(a))))

x

y = ((math.cos(a)+math.sin(a)))/ ((math.cos(a)-math.sin(a)))

if x ==y:
  print("Not equal")
else: 
    print("LHS = RHS")