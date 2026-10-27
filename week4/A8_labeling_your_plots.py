"""Activity 8 10/1/2026 Theo Buckridge
Labeling your plots.
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

plt.title('x and y components')
plt.xlim(0,5)
plt.ylim(-10,10)
plt.xlabel('t',size=15)
plt.ylabel('x(t),y(t)',size=15)

plt.plot(xs,f_1(xs), 'r:o', label='x(t)')
# plt.show()

plt.plot(xs,f_2(xs), 'g--*', label='y(t)')
plt.legend()
plt.show()

plt.title('parametric plot')
plt.xlim(-10,10)
plt.ylim(-10,10)
plt.xlabel('x(t)',size=15)
plt.ylabel('y(t)',size=15)
plt.plot(f_1(xs),f_2(xs), 'b-D')
plt.show()