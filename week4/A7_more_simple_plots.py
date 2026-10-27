"""Activity 7 10/1/2026 Theo Buckridge
More simple plots.
"""

import numpy as np
from numpy import cos, sin, sqrt, pi, e
import matplotlib.pyplot as plt

def f_1(x):
    return cos(x**2)*cos(x)+x*cos(x)
def f_2(x):
    return cos(x**2)*sin(x)+x*sin(x)

xs = np.linspace(0,5,21)
print(xs)

plt.xlim(0,5)
plt.ylim(-10,10)
plt.plot(xs,f_1(xs), 'r:o')
# plt.show()

plt.plot(xs,f_2(xs), 'g--*')
plt.show()

plt.xlim(-10,10)
plt.ylim(-10,10)
plt.plot(f_1(xs),f_2(xs), 'b-D')
plt.show()