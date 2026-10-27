"""Activity 9 10/13/2026 Theo Buckridge
Try using Dfit to fit a model to the LIGO data for the first observed black hole merger.
"""

import numpy as np
from numpy import cos,sin,sqrt,exp
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit

# a)
data = pd.read_csv('H1-STRAIN-1126259462-0.csv')
c0,c1 = list(data)

ts = data[c0].to_numpy()
hs = data[c1].to_numpy()
t0 = ts[0]
t0s = ts - t0

# plt.plot(t0s,hs,'b-')
# ymax = max(hs)
# plt.ylim(-2*ymax,2*ymax)
# plt.xlabel(c1)
# plt.xlabel(c0)
# plt.show()

# b)
g = 6.67e-11
c = 299792458
delta = 0.001
def bhmerge(t,aa,tc,phi0,mc2):
    hhs = np.zeros_like(t)
    tcts = tc - t
    wheretct = np.nonzero(tcts>delta)
    tctws = tcts[wheretct]
    hsw = aa*tctws**(-1/4)*cos(phi0 - 2*(tctws/(5*mc2))**(5/8))
    hhs[wheretct] = hsw
    return hhs
# mc2 = M_c*g/c**3





guesses = (0.5,0.25,0,2e-4)

# hsnew = bhmerge(t0s,*guesses)
# plt.plot(t0s,hs,'b-') # plot the data 
# plt.plot(t0s,hsnew,'r-')
# plt.xlabel(c0)
# plt.ylabel(c1)
# plt.show()



(aa,tc,phi0,mc2),cc = curve_fit(bhmerge,t0s,hs,p0=guesses)
tmin = min(t0s)
tmax = max(t0s)
tmod = np.linspace(tmin,tmax,1000)
hmod = bhmerge(tmod,aa,tc,phi0,mc2)
plt.plot(t0s,hs,'b-') # plot the data
plt.plot(tmod,hmod,'r') # plot the model
plt.xlabel(c0)
plt.ylabel(c1)
print(f't_c={tc}, phi0={phi0}, mc2={mc2}')
plt.show()