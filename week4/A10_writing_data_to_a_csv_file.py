"""Activity 10 9/29/2026 Theo Buckridge
Writing data to a csv file.
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

rows = int(input('rows? '))
cols = 3
myar = np.zeros((rows,cols),int)
for r in range(rows):
    for c in range(cols):
        myar[r,c] = cols*r+c+1
print('Array:\n',myar)

np.savetxt('foo.csv',myar,newline='\r\n',fmt='%10.6f', header='C1, C2, C3', comments12='', delimiter=',')