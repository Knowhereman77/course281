"""Activity 9 10/8/2026 Theo Buckridge
Create and use a Data class.
"""

import numpy as np
from numpy import cos,sin,sqrt,newaxis,pi
import matplotlib.pyplot as plt

class Data:
    """An object that holds two lists of data.
    """
    def __init__(self,x=['x'],y=['y']):
        self.x = x
        self.y = y
    
    def plot(self):
        X = self.x[1:]
        Y = self.y[1:]
        plt.plot(X,Y,'m-o')
        plt.xlabel(self.x[0])
        plt.ylabel(self.y[0])
        plt.show()
    def to_numpy(self,colname):
        if self.x[0] == colname:
            return np.array(self.x[1:])
        elif self.y[0] == colname:
            return np.array(self.y[1:])
        else:
            return


falldata = Data(['times',0.332,0.300,0.251],['heights',1.0,0.8,0.6])

falldata.plot()

print(falldata.to_numpy('heights'))
print(falldata.to_numpy('times'))
