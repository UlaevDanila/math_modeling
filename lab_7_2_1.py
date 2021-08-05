import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

fig, ax = plt.subplots()

anim_object, = plt.plot([], [], '-', lw = 2)

xdata, ydata = [], []

ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

def update(frames):
  x = np.sin(frames)*(np.e**np.cos(frames) - 2*np.cos(4*frames) + (np.sin(frames/12))**5)
  y = np.cos(frames)*(np.e**np.cos(frames) - 2*np.cos(4*frames) + (np.sin(frames/12))**5)
  xdata.append(x)
  ydata.append(y)
  anim_object.set_data(xdata, ydata)
  return anim_object,

ani = FuncAnimation(fig, update, frames = np.arange(0, 12*np.pi, 0.1), interval = 10)

ani.save('lab_7_2_1.gif')