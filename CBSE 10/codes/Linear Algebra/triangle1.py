# -*- coding: utf-8 -*-
"""Triangle1.ipynb

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


a= 3
c = 4
e1 = np.array(([1,0]))
e2 = np.array(([0,1]))

C = a*e1
B = np.array(([0,0]))
A = c*e2
D = 0.5*a*e1

x_AB = line_gen(A,B)
x_BC= line_gen(B,C)
x_CA = line_gen(C,A)
x_AD = line_gen(A,D)
x_BD = line_gen(B,D)
x_DC = line_gen(D,C)

plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
plt.plot(x_AD[0,:],x_AD[1,:],label='$AD$')
plt.plot(x_BD[0,:],x_BD[1,:],label='$BD$')
plt.plot(x_DC[0,:],x_DC[1,:],label='$DC$')
tri_coords = np.vstack((A,B,C,D)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','C','D']
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

