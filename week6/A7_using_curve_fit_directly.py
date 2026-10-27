"""Activity 7 10/13/2026 Theo Buckridge
Try using curve_fit directly without the Dfit wrapper.
"""

import numpy as np
from numpy import cos,sin,sqrt,exp
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit

peak4 = pd.read_excel('peak4.xlsx')
c0,c1 = list(peak4)
xs = peak4[c0].to_numpy()
ys = peak4[c1].to_numpy()

def gauss(x,aa,x0,w,bb0,bb1,bb2):
    """Model function: Gaussian plus linear background"""
    return aa*exp(-(x-x0)**2/(2*w**2)) + bb0 + bb1*x + bb2*x**2

guesses = (1,0,1,0,0,0)
(aa,x0,w,bb0,bb1,bb2),cc = curve_fit(gauss,xs,ys,p0=guesses)

xmin = min(xs)
xmax = max(xs)
xmod = np.linspace(xmin,xmax,500)
ymod = gauss(xmod,aa,x0,w,bb0,bb1,bb2)

plt.plot(xs,ys,'bo') # plot the data
plt.plot(xmod,ymod,'r') # plot the model
plt.xlabel(c0)
plt.ylabel(c1)
plt.show()