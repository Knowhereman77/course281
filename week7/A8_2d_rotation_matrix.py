"""Activity 8 10/13/2026 Theo Buckridge
Try using a 2D Rotation matrix.
"""

import numpy as np
from numpy import cos,sin,pi
from scipy import linalg


# a)
for theta in (1,2,-1.4,2.3):
    r_theta = np.array(((cos(theta),-1*sin(theta)),(sin(theta),cos(theta))))
    print(f'theta = {theta}: R_theta*R_theta^T = {r_theta@r_theta.T}')

# b)
for theta in (pi/4,pi/2,pi,3*pi/2):
    r_theta = np.array(((cos(theta),-1*sin(theta)),(sin(theta),cos(theta))))
    r = np.array((1,0))
    print(f'theta = {theta}: R_theta*r = {r_theta@r}')

# b)
