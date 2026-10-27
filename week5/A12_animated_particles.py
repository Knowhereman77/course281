"""Activity 12 10/8/2026 Theo Buckridge
animate the bouncing particles.
"""

import numpy as np
from numpy import cos,sin,sqrt,newaxis,pi
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

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


tmax = 8
nf = 201
dt = tmax/(nf-1)

p = Mass(0,0,1,10)


xmax = tmax*p.vx

plt.rc('font', size=16)
fig = plt.figure()
ax = plt.axes(xlim=(0,xmax*1.1), ylim=(-1,10))
line, = ax.plot([], [], lw=2)
label = plt.text(xmax-3,-0.5,'')
plt.xlabel('x(t)')
plt.ylabel('y(t)')
plt.title('falling masses')

def init():
    line.set_data([],[])
    label.set_text('')
    return line,label

def animate(i):
    p.step(dt)
    t = dt*i
    line.set_data(p.xs,p.ys)
    label.set_text('t = {:.3f}'.format(t))
    return line,label

anim = FuncAnimation(fig, animate, init_func=init, frames=nf, interval=1000*dt, blit=True, repeat=False)
plt.show()