"""ints.py 10/27/2026 Theo Buckridge
Try out numerical integration methods.
"""

import numpy as np
from numpy import cos,sin,pi

def trap(f,a,b,nn):
    """trapezoid-rule integration of f from a to b with nn slices"""
    h = (b-a)/nn
    wts = np.ones(nn+1)
    wts[0] = 0.5
    wts[-1] = 0.5
    xs = np.linspace(a,b,nn+1)
    # print(wts)
    fs = f(xs)
    return h*np.sum(fs*wts)

def igrand(x):
    return sin(x)

bb = 3
print(f'exact: {1-cos(bb)}')
for nn in (5,10,20):
    print(f'trap result with {nn} slices = {trap(igrand,0,bb,nn)}')