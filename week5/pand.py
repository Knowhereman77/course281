"""pand.py 10/6/2026 Theo Buckridge
try out panda.
"""

import numpy as np
from numpy import cos,sin
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('gl2_missing.xlsx')
# print(type(df))
# print(list(df))
xs = df['x'].to_numpy()
ys = df['y'].to_numpy()
plt.plot(xs,ys,'b-o')
plt.show()