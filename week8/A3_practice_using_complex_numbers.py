"""Activity 3 10/27/2026 Theo Buckridge
Practice using complex numbers in python.
"""

import numpy as np
from numpy import cos,sin,exp,e
import matplotlib.pyplot as plt


# a)

print('(3+4i)/(5+6i) = ?')
print(f'My answer = 39/61 + i*2/61 = {(39+2j)/61}')
print(f'Python answer = {(3+4j)/(5+6j)}')

# b)

print('e^2i = ?')
print(f'My answer = cos(2) + i*sin(2) = {cos(2) + sin(2)*1j}')
print(f'Python answer = {exp(2j)}')

print('cos(3i) = ?')
print(f'My answer = (e^3 + 1/e^3)/2 = {(e**3 + 1/e**3)/2}')
print(f'Python answer = {cos(3j)}')

# c)

z = 5.0 + 0.2j
def f(t):
    return exp(z*t*1j)

ts = np.linspace(0,10,300)
fs = f(ts)

plt.subplot(121)
plt.plot(ts, fs.real, 'r-',label='Re[f(t)]')
plt.plot(ts, fs.imag, 'b-',label='Im[f(t)]')
plt.xlabel('t')
plt.legend()

plt.subplot(122)
plt.plot(fs.real,fs.imag,label='f(t)')
plt.xlabel('Re[f(t)]')
plt.ylabel('Im[f(t)]')
plt.legend()

plt.tight_layout()
plt.show()

