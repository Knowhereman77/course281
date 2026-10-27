"""Activity 5 9/29/2026 Theo Buckridge
Writing an array to a text file.
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

np.savetxt('foo.txt',myar)