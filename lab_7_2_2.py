import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

fig, ax = plt.subplots()

anim_object, = plt.plot([], [], '-', lw = 2)

xdata, ydata = [], []

ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)

def update(frames):
  x = 16*(np.sin(frames))**3
  y = 13*np.cos(frames) - 5*np.cos(2*frames) - 2*np.cos(3*frames) - np.cos(4*frames)
  xdata.append(x)
  ydata.append(y)
  anim_object.set_data(xdata, ydata)
  return anim_object,

ani = FuncAnimation(fig, update, frames = np.arange(0, 2*np.pi, 0.1), interval = 10)

ani.save('lab_7_2_2.gif')