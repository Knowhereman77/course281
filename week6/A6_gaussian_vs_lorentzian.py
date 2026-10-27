"""Activity 6 10/13/2026 Theo Buckridge
Testing if a gaussian or lorentzian model is a better fit for the data in gl1.xlsx and gl2.xlsx.
"""

import numpy as np
from numpy import cos,sin,sqrt,exp
import matplotlib.pyplot as plt
import pandas as pd
from dfit import Dfit

data1 = pd.read_excel('gl1.xlsx')
c01,c11 = list(data1)
xs1 = data1[c01].to_numpy()
ys1 = data1[c11].to_numpy()

data2 = pd.read_excel('gl2.xlsx')
c02,c12 = list(data1)
xs2 = data2[c02].to_numpy()
ys2 = data2[c12].to_numpy()


def gauss(x,A,x0,w,B):
    """Model function: Gaussian plus constant background"""
    return A*exp(-(x-x0)**2/(2*w**2)) + B

def lorentz(x,A,x0,w,B):
    """Model function: Lorentzian plus constant background"""
    return A/(1+((x-x0)/w)**2) + B

guesses1_gauss = [1,0,1,-0.2]
p1_gauss_fit = Dfit(gauss,xs1,ys1,p0s=guesses1_gauss)

guesses1_lorentz = [1,0,1,-0.2]
p1_lorentz_fit = Dfit(lorentz,xs1,ys1,p0s=guesses1_lorentz)

guesses2_gauss = [1.6,0,1,-0.4]
p2_gauss_fit = Dfit(gauss,xs2,ys2,p0s=guesses1_gauss)

guesses2_lorentz = [1.6,0,1,-0.4]
p2_lorentz_fit = Dfit(lorentz,xs2,ys2,p0s=guesses1_lorentz)

p1_gauss_fit.plotfit(xlabel=c01,ylabel=c11)
p1_gauss_fit.printfit()

p1_lorentz_fit.plotfit(xlabel=c01,ylabel=c11)
p1_lorentz_fit.printfit()

p2_gauss_fit.plotfit(xlabel=c02,ylabel=c12)
p2_gauss_fit.printfit()

p2_lorentz_fit.plotfit(xlabel=c02,ylabel=c12)
p2_lorentz_fit.printfit()


# for the data in gl1.xlsx, the lorentzian fit has a much better reduced chi-squared,
# of 0.00204 vs. 0.005302, so lorentzian describes the data better.

# for the data in gl2.xlsx, the gaussian fit has a much better reduced chi-squared,
# of 0.0.002123 vs. 0.0.004606, so gaussian describes the data better.



