"""Activity 5 10/27/2026 Theo Buckridge
Numerical integration using the trapezoid rule.
"""

import numpy as np
from numpy import cos,sin,exp,e
from scipy import integrate

def f(x):
    return x*sin(x**2)

a = 1
b = 5

exact = (cos(a**2) - cos(b**2))/2
integral = integrate.quad(f,a,b)[0]


# a)

nn = int(input('Enter a number of slices N>0: '))
if (nn >= 1):

    h = (b-a)/nn
    # b)

    wts = np.ones(nn+1)
    wts[0] = 0.5
    wts[-1] = 0.5
    xs = np.linspace(a,b,nn+1)
    fs = f(xs)
    i_trap = h*np.sum(wts*fs)

    # c)

    print(f'Exact value = {exact}')
    print(f'Integrated value = {integral}')
    print(f'Value using trapezoid rule = {i_trap}')
    # N = 15823 to compute value to six digits
    # N = 
