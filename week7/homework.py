# Make a 3d scatter plot of an imaginary galaxy and rotate it
import numpy as np
from numpy import cross,pi
import matplotlib.pyplot as plt
from scipy import linalg
import pandas as pd

galaxy = pd.read_csv('galaxy2.txt',sep=r'\s+')
c0,c1,c2 = list(galaxy)
xs = galaxy[c0].to_numpy()
ys = galaxy[c1].to_numpy()
zs = galaxy[c2].to_numpy()

def rmat(theta,nhat):
    return linalg.expm(cross(np.eye(3),nhat*theta))

plt.figure(figsize=(10,10))
plt.rc('font', size=12)
ax = plt.axes(projection='3d')
ax.scatter(xs,ys,zs,s=1,c='b')
ax.set_xlabel(c0)
ax.set_ylabel(c1)
ax.set_zlabel(c2)
plt.title('Imaginary galaxy')
plt.show()

rot_axis = np.array((1,0,0))
rot_axis = rot_axis/linalg.norm(rot_axis)
theta_rot = pi/2

rot_mat = rmat(theta_rot,rot_axis)

xs_rot,ys_rot,zs_rot = rot_mat@(xs,ys,zs)


plt.figure(figsize=(10,10))
plt.rc('font', size=12)
ax = plt.axes(projection='3d')
ax.scatter(xs_rot,ys_rot,zs_rot,s=1,c='r')
ax.set_xlabel(c0)
ax.set_ylabel(c1)
ax.set_zlabel(c2)
plt.title('Imaginary galaxy, rotated pi/2 rad about x-axis')
plt.show()

v = np.array((0,0,1))

print(rot_mat)

