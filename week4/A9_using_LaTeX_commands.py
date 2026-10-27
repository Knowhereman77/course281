"""Activity 9 10/1/2026 Theo Buckridge
Use LaTeX commands in your plot labels.
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

plt.title('x and y components',size=20)
plt.xlim(0,5)
plt.ylim(-20,20)
plt.xlabel('t',size=15)
plt.ylabel(r'$x(\pi t),y(\pi t)$',size=15)

plt.plot(xs,f_1(pi*xs), 'r:o', label=r'$x(\pi t)$')
# plt.show()

plt.plot(xs,f_2(pi*xs), 'g--*', label=r'$y(\pi t)$')
plt.legend()
plt.show()

plt.title('parametric plot',size=20)
plt.xlim(-20,20)
plt.ylim(-20,20)
plt.xlabel(r'$x(\pi t)$',size=15)
plt.ylabel(r'$y(\pi t)$',size=15)
plt.plot(f_1(pi*xs),f_2(pi*xs), 'b-D')
plt.show()