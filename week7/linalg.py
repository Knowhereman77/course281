"""linalg.py 10/13/2026 Theo Buckridge
Try out linear algebra with scipy.
"""

import numpy as np
from numpy import cos,sin,sqrt
import matplotlib.pyplot as plt
from scipy import linalg


# make two vectors, compute various products
# a = np.array((1,2,3),float)
# b = np.array((4,5,6),float)
# print(f'a = {a}  b = {b}')
# print(f'a*b = {a*b}')
# print(f'a@b = {a@b}')
# print(f'a dot b = {np.dot(a,b)}')
# print(f'a cross b = {np.cross(a,b)}')


# aa = np.array(((1,2,3),(4,5,6)))
# bb = np.array(((5,6),(7,8),(9,10)))
# print(f'aa =\n{aa}\nbb =\n{bb}')
# print(f'aa@bb =\n{aa@bb}')
# print(f'matmul(aa,bb) =\n{np.matmul(aa,bb)}')

# mm = np.array(((1,2),(3,4)))
# print(mm)
# mminv = linalg.inv(mm)
# print(mminv)
# print(mminv@mm)
# print(linalg.det(mm),linalg.det(mminv))

# mm = np.array(((2,1,4,1),(3,4,-1,-1),(1,-4,1,5),(2,-2,1,3)))
# print(mm)
# r = np.array((-4,3,9,7))
# print(r)

# w,x,y,z = linalg.inv(mm)@r
# print(w,x,y,z)

# w,x,y,z = linalg.solve(mm,r)
# print(w,x,y,z)

dd = np.array(((2,-1),(-1,2)))
evals,evecs = linalg.eigh(dd)
print(evecs[0],evals[0])
print(evecs[1],evals[1])
