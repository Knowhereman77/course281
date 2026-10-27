"""Activity 7 10/13/2026 Theo Buckridge
Practice solving a system of linear equations.
"""

import numpy as np
from scipy import linalg

aa = np.array(((1,4,1),(4,-1,-1),(2,1,3)))
b = np.array((-4,3,7))

# a)
x,y,z = linalg.inv(aa)@b
print(x,y,z)

# b)
x,y,z = linalg.solve(aa,b)
print(x,y,z)

xx = (x,y,z)

print(f'b = {b}')
print(f'Ax = {aa@xx}')
