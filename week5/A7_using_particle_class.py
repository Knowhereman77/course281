"""Activity 7 10/8/2026 Theo Buckridge
Practice using Particle objects.
"""

import numpy as np
from numpy import cos,sin,sqrt,pi
import matplotlib.pyplot as plt

class Particle:
    """Particle in 2D, position (default x and y are zero).
    """
    def __init__(self,x=0.0,y=0.0):
        self.x = x
        self.y = y

cparts = []
for x in np.linspace(-5,5,40):
    for y in np.linspace(-5,5,40):
        r = sqrt(x**2 + y**2)
        if r <= 5 and r >= 3:
            cparts.append(Particle(x,y))
for p in cparts:
    plt.plot(p.x,p.y,'mo')
ax = plt.gca()
ax.axis('equal')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

R = 10
N = 50
allparticles = []
for n in range(0,N):
    theta = 2*pi*n/N
    allparticles.append(Particle(R*cos(theta),R*sin(theta)))
for p in allparticles:
    plt.plot(p.x,p.y,'mo')
ax = plt.gca()
ax.axis('equal')
plt.xlabel('x')
plt.ylabel('y')
plt.show()