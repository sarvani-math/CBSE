# -*- coding: utf-8 -*-
"""5.(iv).ipynb

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

!cp /content/gdrive/MyDrive/CoordGeo/line/line_funcs.py /content
!cp /content/gdrive/MyDrive/CoordGeo/triangle/triangle_funcs.py /content
!cp /content/gdrive/MyDrive/CoordGeo/conics/conics_funcs.py /content 
!cp /content/gdrive/MyDrive/CoordGeo/params.py /content

def f(x): 
  fval =  (x**4) + x**3 - 14*x**2- 2*x + 24
  return fval

fvec = np.vectorize(f)
x = np.linspace(-5,10,100)

##Input parameters
plt.plot(x,fvec(x),label='quadratic')
#
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor


plt.show()
