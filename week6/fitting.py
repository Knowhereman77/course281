"""fitting.py 10/13/2026 Theo Buckridge
Try out fitting.
"""

import numpy as np
from numpy import cos,sin,sqrt
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit
from dfit import Dfit

# read data file and print the column names
# data1 = pd.read_excel('data1.xlsx')
# print(list(data1))
# extract to arrays
# c0,c1,c2 = list(data1)
# xs = data1[c0].to_numpy()
# ys = data1[c1].to_numpy()
# yerrs = data1[c2].to_numpy()

wavedata = pd.read_excel('wavedata.xlsx')
w0,w1 = list(wavedata)
ts = wavedata[w0].to_numpy()
ys = wavedata[w1].to_numpy()

def linmod(x,p0,p1):
    """linear model"""
    return p0 + p1*x

def quadmod(x,p0,p1,p2):
    """quadratic model"""
    return p0 + p1*x + p2*x**2

def pmod(x,p0,p1,p2,p3,p4):
    """quartic model"""
    return p0 + p1*x + p2*x**2 + p3*x**3 + p4*x**4

def wmod(t,aa,omega,phi,bb):
    """osc model"""
    return aa*cos(omega*t+phi) + bb


# plot the data
plt.plot(ts,ys,'g+')
plt.xlabel(w0)
plt.ylabel(w1)

# plot the model
# xmods = np.linspace(xs[0],xs[-1],300)
# p0 = 37.0
# p1 = -2.0
# ymods = linmod(xmods,p0,p1)
# plt.plot(xmods,ymods,'b-')
# plt.show()

# use Dfit to fit the data
guesses = [0,0.6,0,0]
wfit = Dfit(wmod,ts,ys,p0s=guesses)
wfit.printfit()
wfit.plotfit()
plt.show()