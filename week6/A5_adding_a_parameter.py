"""Activity 5 10/13/2026 Theo Buckridge
Adding a parameter to fit the data in peak4.xlsx.
"""

import numpy as np
from numpy import cos,sin,sqrt,exp
import matplotlib.pyplot as plt
import pandas as pd
from dfit import Dfit

peak4 = pd.read_excel('peak4.xlsx')
c0,c1 = list(peak4)
xs = peak4[c0].to_numpy()
ys = peak4[c1].to_numpy()

def gauss(x,aa,x0,w,bb0,bb1,bb2):
    """Model function: Gaussian plus linear background"""
    return aa*exp(-(x-x0)**2/(2*w**2)) + bb0 + bb1*x + bb2*x**2

guesses = [3,5,1,1,0,0]   # parameter guesses
p4fit = Dfit(gauss,xs,ys,p0s=guesses)


p4fit.plotfit(xlabel=c0,ylabel=c1)
p4fit.printfit()

# adding a parameter is justified,
# since the reduced chi-squared drops from 0.01757 to 0.009957,
# a fairly significant difference
