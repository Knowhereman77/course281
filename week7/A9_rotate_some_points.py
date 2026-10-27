"""Activity 9 10/13/2026 Theo Buckridge
Plot some rotated points.
"""

import numpy as np
from numpy import cos,sin,pi
from scipy import linalg
import matplotlib.pyplot as plt

def r_theta(theta):
    return np.array(((cos(theta),-1*sin(theta)),(sin(theta),cos(theta))))

rng = np.random.default_rng()

x = rng.normal(size=100)
y = rng.normal(size=100)

v = np.array((x,y))

plt.plot(x,y,'ro',label='0 rad')
plt.legend()

theta = 0.1
xr,yr = r_theta(theta)@v

plt.plot(xr,yr,'go',label='0.1 rad')
plt.legend()

theta = pi/2
xr,yr = r_theta(theta)@v

plt.plot(xr,yr,'bo',label='pi/2 rad')
plt.legend()
plt.show()