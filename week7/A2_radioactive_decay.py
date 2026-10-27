"""Activity 2 10/13/2026 Theo Buckridge
Plotting the data and uncertainties of radioactive decay data.
"""

import numpy as np
from numpy import cos,sin,sqrt
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

plt.subplot(121)
plt.plot(ts1,ns1,'bo')
plt.xlabel(c01)
plt.ylabel(c11)

plt.subplot(122)
plt.plot(ts2,ns2,'go')
plt.xlabel(c02)
plt.ylabel(c12)
plt.tight_layout()
plt.show()

nerrs1 = sqrt(ns1)
nerrs2 = sqrt(ns2)

plt.subplot(121)
plt.errorbar(ts1,ns1,nerrs1,fmt='bo',capsize=5)
plt.xlabel(c01)
plt.ylabel(c11)
plt.yscale('log')

plt.subplot(122)
plt.errorbar(ts2,ns2,nerrs2,fmt='go',capsize=5)
plt.xlabel(c02)
plt.ylabel(c12)
plt.yscale('log')
plt.tight_layout()
plt.show()