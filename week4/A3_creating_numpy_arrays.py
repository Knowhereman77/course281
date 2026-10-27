"""Activity 3 9/29/2026 Theo Buckridge
Creating numpy arrays.
"""

import numpy as np
import matplotlib.pyplot as plt

rows = int(input('rows? '))
cols = int(input('cols? '))
myar = np.zeros((rows,cols),int)
for r in range(rows):
    for c in range(cols):
        myar[r,c] = cols*r+c+1
print('Array:\n',myar)