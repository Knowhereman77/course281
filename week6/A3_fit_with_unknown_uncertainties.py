"""Activity 3 10/13/2026 Theo Buckridge
Practice fitting data with unknown uncertainties.
"""

import numpy as np
from numpy import cos,sin,sqrt
import matplotlib.pyplot as plt
import pandas as pd
from dfit import Dfit

data3 = pd.read_excel('data3.xlsx')
c0,c1 = list(data3)
xs = data3[c0].to_numpy()
ys = data3[c1].to_numpy()

def polynomial(x,p0,p1,p2,p3,p4,p5):
    """Model function is polynomial up to x**5"""
    return (p0 + p1*x + p2*x**2 + p3*x**3 + p4*x**4 + p5*x**5)

linfit = Dfit(polynomial,xs,ys,varies=[True,True])
quadfit = Dfit(polynomial,xs,ys,varies=[True,True,True])
cubfit = Dfit(polynomial,xs,ys,varies=[True,True,True,True])
quarfit = Dfit(polynomial,xs,ys,varies=[True,True,True,True,True])
quinfit = Dfit(polynomial,xs,ys,varies=[True,True,True,True,True,True])


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

# Cubic fit is best!