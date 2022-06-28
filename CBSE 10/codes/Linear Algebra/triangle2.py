# -*- coding: utf-8 -*-
"""Triangle2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GvuGl_svfgTfgLcmydFs9PfnODPn8p54
"""


import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
from numpy import linalg as LA
import sys

sys.path.insert(0, '/Users/gvv/Desktop/CoordGeo')        #path to my scripts

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen



a= 4
s = 3
c = 5

b = mp.acos(a/(2*c))
A1 = np.array([c*mp.cos(b),c*mp.sin(b)]) 
A = np.around(A1, decimals=2)
B = np.array([0,0]) 
C = a*e1 
D = 0.5*a*e1
E = -s*e1
F = np.array([0.84*a,(c*mp.sin(b))/3])

x_AB = line_gen(A,B)
x_BC= line_gen(B,C)
x_CA = line_gen(C,A)
x_AD = line_gen(A,D)
x_BD = line_gen(B,D)
x_DC = line_gen(D,C)
x_BE = line_gen(B,E)
x_EF = line_gen(E,F)

plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
plt.plot(x_AD[0,:],x_AD[1,:],label='$AD$')
plt.plot(x_BD[0,:],x_BD[1,:],label='$BD$')
plt.plot(x_DC[0,:],x_DC[1,:],label='$DC$')
plt.plot(x_BE[0,:],x_BE[1,:],label='$BE$')
plt.plot(x_EF[0,:],x_EF[1,:],label='$EF$')
tri_coords = np.vstack((A,B,C,D,E,F)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','C','D','E','F']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.show()
