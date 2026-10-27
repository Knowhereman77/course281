"""Activity 10 10/13/2026 Theo Buckridge
Rotate some points in 3d around different axes.
"""

import numpy as np
from numpy import cos,sin,pi,cross
from scipy import linalg

def rmat(theta,nhat):
    return linalg.expm(cross(np.eye(3),nhat*theta))

v1 = np.array((0,2,0))
v2 = np.array((0,0,3))

directions = ['x','y','z']
norms = np.array([[1,0,0],[0,1,0],[0,0,1]])
norms = np.array([n/linalg.norm(n) for n in norms])
theta_rot = pi/2

print(f'v1 = {v1}')
print(f'v2 = {v2}')

for i in range(3):
    print('\n')
    rot_mat = rmat(theta_rot,norms[i])
    print(f'rotation by pi/2 about {directions[i]} =\n{rot_mat}')
    print(f'applied to v1 = {rot_mat@v1}')
    print(f'applied to v2 = {rot_mat@v2}')

