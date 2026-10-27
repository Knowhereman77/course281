"""oop.py 10/8/2026 Theo Buckridge
Try out object oriented programming in python"""

import numpy as np
from numpy import cos,sin,sqrt,newaxis
import matplotlib.pyplot as plt
import pandas as pd

class Spammer:
    # you need this definition for a useful class
    # for all class methods start with arg "self" (means this object)
    def __init__(self,x): 
        self.x = x

    def pr(self,n):
        print(n*self.x)

# make two Spammer's (instantiating): 
hah = Spammer('hah ')
hee = Spammer('hee ')
# when you call a class method, use all args except self

# class inheritance: Eggs stars as a Spammer, gets all the methods from Spammer
class Eggs(Spammer):
    def __init__(self):
        # this just is how it is
        super().__init__('Eggs! ')
    def pr(self,n):
        super().pr(n)
        print('That\'s all')

class Part:
    """Class to represent a particle at position x,y.
    """
    def __init__(self,x=0.,y=0.):
        self.x = x
        self.y = y

def showparticles(allparts):
    """Plot the positions of the Particles in the list allparts.
    """
    for p in allparts:
        plt.plot(p.x,p.y,'mo')
    plt.show()

ps = []
for x in np.linspace(-3,3,50):
    for y in np.linspace(-3,3,50):
        r = sqrt(x**2+y**2)
        if r < 2:
            ps.append(Part(x,y))
ax = plt.gca()
ax.axis('equal')
showparticles(ps)