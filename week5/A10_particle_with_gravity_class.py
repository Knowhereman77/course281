"""Activity 10 10/8/2026 Theo Buckridge
Create a class for particles that move with gravity.
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
        self.x += self.vx*dt
        self.y += self.vy*dt 
        self.vy -= G*dt
        self.xs.append(self.x)
        self.ys.append(self.y)

    def trajectory(self):
        plt.plot(self.xs,self.ys,'m-o')


dt = 0.01

p = Mass(0,0,1,1)

while p.x == 0 or p.y > 0:
    p.step(dt)
p.trajectory()
plt.xlabel('x(t)')
plt.ylabel('y(t)')
plt.title('falling mass')
plt.show()

mlist = [Mass(0,0,1,1),Mass(.1,0,2,1),Mass(0,.1,1,2),Mass(.1,.1,2,2)]

for m in mlist:
    while len(m.xs)==1 or m.y > 0:
        m.step(dt)
    m.trajectory()
plt.xlabel('x(t)')
plt.ylabel('y(t)')
plt.title('falling masses')
plt.show()