"""Activity 5 10/8/2026 Theo Buckridge
Make a 3D surface plot of an atomic orbital (310).
"""

import numpy as np
from numpy import cos,sin,sqrt,newaxis,exp
import matplotlib.pyplot as plt


def phi(x,y):
    r = sqrt(x**2+y**2)
    return x*(6-r)*exp(-1*r/3)


xs = np.linspace(-20,20,100)
ys = np.linspace(-20,20,100)[:,newaxis]
fs = phi(xs,ys)
plt.imshow(fs)
plt.colorbar()
plt.title(r'$\psi(x,y)$')
plt.show()

