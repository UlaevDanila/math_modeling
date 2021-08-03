import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

fig, ax = plt.subplots()

anim_object, = plt.plot([], [], '-', lw = 2)

xdata, ydata = [], []

r = float(input("Введите радиус: "))

ax.set_xlim(0, 15*r)
ax.set_ylim(-3*r, 3*r)

def update(alpha):
    x = r*(alpha - (np.sin(alpha)))
    y = r*(1-(np.cos(alpha)))
    xdata.append(x)
    ydata.append(y)
    anim_object.set_data(xdata, ydata)
    return anim_object,

ani = FuncAnimation(fig, update, frames = np.arange(-3*np.pi, 3*np.pi,0.1), interval = 10)

ani.save('lab_7_1.gif')