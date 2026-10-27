"""Activity 5 10/13/2026 Theo Buckridge
Practice multiplying matrices.
"""

import numpy as np

aa = np.array(((1,3),(2,4),(5,6)))
bb = np.array(((2,1,4),(3,2,1)))

# u dot v = uvcos(theta) = 2*sqrt(2)*cos(pi/4)= 2*sqrt(2)*1/sqrt(2) = 2
# u dot v = 2
print(f'A =\n{aa}')
print(f'B =\n{bb}')
print(f'A*B =\n{aa@bb}')
print(f'B*A =\n{bb@aa}')

# C = A*B, C00 = A00*B00 + A01*B10 = 1*2 + 3*3 = 2 + 9 = 11
# C = B*A, C00 = B00*A00 + B01*A10 + B02*A20 = 2*1 + 1*2 + 4*5 = 2 + 2 + 20 = 24
