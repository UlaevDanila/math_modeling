import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

fig, ax = plt.subplots()

anim_object, = plt.plot([], [], '-', lw = 2)

xdata, ydata = [], []

ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

def circle(r):
    f = np.linspace(0, 2*np.pi, 100)
    x = r*np.cos(f)
    y = r*np.sin(f)
    return x,y

def update(frames):
  anim_object.set_data(circle(frames)[0], circle(frames)[1])
  return anim_object,

ani = FuncAnimation(fig, update, frames = np.arange(0, 5, 0.1), interval = 10)

ani.save('lab_7_3.gif')