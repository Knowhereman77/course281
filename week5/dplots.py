"""dplots.py 10/6/2026 Theo Buckridge
try out 3d plots.
"""

import numpy as np
from numpy import cos,sin,sqrt,newaxis
import matplotlib.pyplot as plt
import pandas as pd

# define a funtion of two vars
def f(x,y):
    r = sqrt(x**2+y**2)
    return cos(r)

pts = 1000
xs = np.linspace(-20,20,pts)
ys = np.linspace(-20,20,pts)[:,newaxis]

# print(xs)
# print(ys)
fs = f(xs,ys) # broadcasting
# print(fs)

# plt.imshow(fs)
# plt.colorbar()

ax = plt.axes(projection='3d')
ax.plot_surface(xs,ys,fs,cmap='plasma')
ax.set_zlim(-4,4)
plt.show()