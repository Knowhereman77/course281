"""Activity 4 10/27/2026 Theo Buckridge
Numerical integration using scipy.integrate.quad.
"""

import numpy as np
from numpy import cos,sin,exp,e
import matplotlib.pyplot as plt
from scipy import integrate

def f(x):
    return x*sin(x**2)

a = 1
b = 5

# a)

exact = (cos(a**2) - cos(b**2))/2
print(f'Exact value = {exact}')

# b)

integral = integrate.quad(f,a,b)[0]
print(f'Integrated value = {integral}')