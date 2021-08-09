import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color = 'r', label = 'Ball')

def cicloida_move(r, angel_vel, time):
    alpha = angel_vel*(np.pi/180)*time
    x = r*(alpha - (np.sin(alpha)))
    y = r*(1-(np.cos(alpha)))
    return x, y

edge = 4
plt.axis('equal')
ax.set_xlim(0 ,15*edge)
ax.set_ylim(-3*edge, 3*edge)

def animate(i):
    ball.set_data(cicloida_move(r = 3, angel_vel = 1, t = i))

ani = animation.FuncAnimation(fig, animate, frames = 180, interval = 30)
ani.save = ("lab_7dop_1_1.gif")