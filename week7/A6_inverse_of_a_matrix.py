"""Activity 6 10/13/2026 Theo Buckridge
Take the inverse of a matrix.
"""

import numpy as np
from scipy import linalg

cc = np.array(((1,3,2),(2,4,1),(5,6,5)))
cc_inv = linalg.inv(cc)
print(f'C = \n{cc}\nC^-1 = \n{cc_inv}\nC^-1 * C = \n{cc_inv@cc}')

# it didn't print quite what I was expecting, because I hadn't considered floatng point errors, but otherwise it is what I was expecting.
