"""Activity 11 10/8/2026 Theo Buckridge
Make the particles bounce.
"""

import numpy as np
from numpy import cos,sin,sqrt,newaxis,pi
import matplotlib.pyplot as plt

G = 9.8

class Mass:
    def __init__(self,x=0.,y=0.,vx=0.,vy=0.,xs=None,ys=None):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        if xs==None:
            self.xs = [x]
        else:
            self.xs = xs
        if ys==None:
            self.ys = [y]
        else:
            self.xs = ys

    
    def step(self,dt):
        ytemp = self.y
        vytemp = self.vy
        self.x += self.vx*dt
        self.y += self.vy*dt 
        self.vy -= G*dt
        e_restitution = 0.707
        if(self.y < 0):
            self.y = ytemp
            self.vy = -1*vytemp*e_restitution-G*dt


        self.xs.append(self.x)
        self.ys.append(self.y)

    def trajectory(self):
        plt.plot(self.xs,self.ys,'m-')


dt = 0.01

mlist = [Mass(0,0,1,10),Mass(0,8,5,5),Mass(30,6,1,0)]

T = 10

for m in mlist:
    for t in range(0,round(T/dt)):
        m.step(dt)
    m.trajectory()
plt.xlabel('x(t)')
plt.ylabel('y(t)')
plt.title('falling masses')
plt.show()