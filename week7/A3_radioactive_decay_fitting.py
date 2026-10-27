"""Activity 3 10/13/2026 Theo Buckridge
Fit the radioactive decay data to find the counting rate, lifetime, and background counting rate.
"""

import numpy as np
from numpy import cos,sin,sqrt,exp
import matplotlib.pyplot as plt
import pandas as pd
from dfit import Dfit

data1 = pd.read_excel('decay1.xlsx')
c01,c11 = list(data1)
ts1 = data1[c01].to_numpy()
ns1 = data1[c11].to_numpy()

data2 = pd.read_excel('decay2.xlsx')
c02,c12 = list(data2)
ts2 = data2[c02].to_numpy()
ns2 = data2[c12].to_numpy()

def expfit(t,n0,tau,bb):
   """Model function is an exponential with background"""
   return n0*exp(-1*t/tau) + bb

nerrs1 = sqrt(ns1)
nerrs2 = sqrt(ns2)

guesses1 = (100,50,10)
expfit1 = Dfit(expfit,ts1,ns1,nerrs1,p0s=guesses1)

guesses2 = (100,50,10)
expfit2 = Dfit(expfit,ts2,ns2,nerrs2,p0s=guesses2)


expfit1.printfit()
expfit2.printfit()

expfit1.plotfit()
expfit2.plotfit()

guesses12 = (100,50,25)
expfit12 = Dfit(expfit,ts1,ns1,nerrs1,p0s=guesses12,varies=[True,True])

guesses22 = (100,50,25)
expfit22 = Dfit(expfit,ts2,ns2,nerrs2,p0s=guesses22,varies=[True,True])


expfit12.printfit()
expfit22.printfit()

expfit12.plotfit()
expfit22.plotfit()
