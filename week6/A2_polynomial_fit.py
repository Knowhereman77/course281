"""Activity 2 10/13/2026 Theo Buckridge
Practice fitting data to a polynomial.
"""

import numpy as np
from numpy import cos,sin,sqrt
import matplotlib.pyplot as plt
import pandas as pd
from dfit import Dfit

data2 = pd.read_excel('data2.xlsx')
c0,c1,c2 = list(data2)
xs = data2[c0].to_numpy()
ys = data2[c1].to_numpy()
yerrs = data2[c2].to_numpy()

def polynomial(x,p0,p1,p2,p3,p4,p5):
    """Model function is polynomial up to x**5"""
    return (p0 + p1*x + p2*x**2 + p3*x**3 + p4*x**4 + p5*x**5)

linfit = Dfit(polynomial,xs,ys,yerrs,varies=[True,True])
quadfit = Dfit(polynomial,xs,ys,yerrs,varies=[True,True,True])
cubfit = Dfit(polynomial,xs,ys,yerrs,varies=[True,True,True,True])
quarfit = Dfit(polynomial,xs,ys,yerrs,varies=[True,True,True,True,True])
quinfit = Dfit(polynomial,xs,ys,yerrs,varies=[True,True,True,True,True,True])


linfit.plotfit(xlabel=c0,ylabel=c1)
linfit.printfit()

quadfit.plotfit(xlabel=c0,ylabel=c1)
quadfit.printfit()

cubfit.plotfit(xlabel=c0,ylabel=c1)
cubfit.printfit()

quarfit.plotfit(xlabel=c0,ylabel=c1)
quarfit.printfit()

quinfit.plotfit(xlabel=c0,ylabel=c1)
quinfit.printfit()

# Linear fit is best!