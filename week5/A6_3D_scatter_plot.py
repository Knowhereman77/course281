"""Activity 6 10/8/2026 Theo Buckridge
Make a 3D scatter plot of points on a sphere.
"""

import numpy as np
from numpy import cos,sin,pi
import matplotlib.pyplot as plt

R = 1
N = 20

xlist = []
ylist = []
zlist = []
theta = np.linspace(0,pi,N)
phi = np.linspace(0,2*pi,N)
for t in theta:
    for p in phi:
        xlist.append(R*sin(t)*cos(p))
        ylist.append(R*sin(t)*sin(p))
        zlist.append(R*cos(t))

plt.figure(figsize=(10,10))
plt.rc('font', size=12)
ax = plt.axes(projection='3d')
ax.scatter(xlist, ylist, zlist)
plt.show()
