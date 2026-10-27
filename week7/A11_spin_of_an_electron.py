"""Activity 11 10/13/2026 Theo Buckridge
Rotate some points in 3d around different axes.
"""

import numpy as np
from numpy import cos,sin,pi,cross
from scipy import linalg

print('h_bar = 1 everywhere')

# b)
sigma_x = np.array(((0,1),(1,0)))
sigma_y = np.array(((0,-1j),(1j,0)))
sigma_z = np.array(((1,0),(0,-1)))

lambdas_x = linalg.eigvalsh(sigma_x)
lambdas_y = linalg.eigvalsh(sigma_y)
lambdas_z = linalg.eigvalsh(sigma_z)

print(f"Eigenvales of J_x: h_bar*{lambdas_x/2}")
print(f"Eigenvales of J_y: h_bar*{lambdas_y/2}")
print(f"Eigenvales of J_z: h_bar*{lambdas_z/2}")

# c)

def comtat(aa,bb):
    return aa@bb - bb@aa
print('\n')
print(f'[J_x,J_y] =\n{comtat(sigma_x,sigma_y)/4}\n')
print(f'[J_y,J_z] =\n{comtat(sigma_y,sigma_z)/4}\n')
print(f'[J_z,J_x] =\n{comtat(sigma_z,sigma_x)/4}\n')

