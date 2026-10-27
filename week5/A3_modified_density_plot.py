"""Activity 3 10/6/2026 Theo Buckridge
Create density plots.
"""

import numpy as np
from numpy import cos,sin,sqrt,newaxis,arctan2
import matplotlib.pyplot as plt


def s(x,y):
    return cos(sqrt(x**2+y**2)+arctan2(y,x))

def u(x,y):
    return cos(sqrt(x**2+y**2)+0.5*arctan2(y,x))

xs = np.linspace(-20,20,100)
ys = np.linspace(-20,20,100)[:,newaxis]
fs = s(xs,ys)
plt.imshow(fs)
plt.show()

fs1 = u(xs,ys)

plt.imshow(fs1)
plt.show()


