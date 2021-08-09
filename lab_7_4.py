aimport matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

fig, ax = plt.subplots()

anim_object, = plt.plot([], [], marker = 'o', lw = 2, color = 'red')

ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

frames = 100

x = np.zeros((frames))
y = np.zeros((frames))
c = 0.3
d = 0.33
x[0] = 0.1
y[0] = 0.1
for i in range(1, frames,1):
    x[i] = x[i-1]**2 - y[i-1]**2 + c
    y[i] = 2*x[i-1]*y[i-1] + d

def update(i):
  anim_object.set_data(x[:i], y[:i])

  return anim_object,

ani = FuncAnimation(fig, update, frames = frames, interval = 10)

ani.save('lab_7_4.gif')