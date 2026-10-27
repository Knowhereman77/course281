"""Activity 4 9/29/2026 Theo Buckridge
Array slicing.
"""

import numpy as np
import matplotlib.pyplot as plt

rows = int(input('rows? '))
cols = int(input('cols? '))
myar = np.zeros((rows,cols),int)
myar_transpose = np.zeros((cols,rows),int)
for r in range(rows):
    for c in range(cols):
        myar[r,c] = cols*r+c+1
        myar_transpose[c,r] = cols*r+c+1
print('Array:\n',myar)

print('Third column:\n', myar[:,2])
print('Fifth row:\n', myar[4])
print('Upper left:\n', myar[:3,:3])
print('Upper right:\n', myar[:3,-3:])
print('Transpose:\n', myar_transpose)