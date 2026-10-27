"""Activity 8 10/8/2026 Theo Buckridge
Create and use a right triangle class.
"""

import numpy as np
from numpy import cos,sin,sqrt,arccos,arcsin,pi
import matplotlib.pyplot as plt

class RightTriangle:
    """Describes a right triangle using the lengths of the two legs.
    """
    def __init__(self,l1=1.,l2=1.):
        self.l1 = l1
        self.l2 = l2
    
    def hyp(self):
        return np.sqrt(self.l1**2+self.l2**2)
    
    def angle1(self):
        return arccos(self.l1/self.hyp())*180/pi

    def angle2(self):
        return arccos(self.l2/self.hyp())*180/pi

t = RightTriangle(1,sqrt(3))
print(t.hyp())
print(t.angle1())
print(t.angle2())

t2 = RightTriangle(1,1)
print(t2.hyp())
print(t2.angle1())
print(t2.angle2())