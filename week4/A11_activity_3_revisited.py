"""Activity 3 9/29/2026 Theo Buckridge
Creating numpy arrays.
"""

import numpy as np
import matplotlib.pyplot as plt

rows = int(input('rows? '))
cols = int(input('cols? '))
myar = np.arange(1,cols*rows+1).reshape(rows,cols)
print('Array:\n',myar)