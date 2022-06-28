

import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
from numpy import linalg as LA
import sys 
import sympy as sym

sys.path.insert(0, '/Users/gvv/Desktop/CoordGeo')        #path to my scripts

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen


r1 = 8
r2 =5 
O = np.array(([0,0]))

x_circ1= circ_gen(O,r1)
x_circ2= circ_gen(O,r2)

plt.plot(x_circ1[0,:],x_circ1[1,:],label='$Circle1$')
plt.plot(x_circ2[0,:],x_circ2[1,:],label='$Circle2$')


plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.show()

