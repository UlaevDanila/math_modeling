import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots() 

anim_object, = plt.plot([], [], '-', lw=2) 
xdata, ydata = [], [] 

ax.set_xlim(-25, 25) 
ax.set_ylim(-25, 25) 

x1 = [2, 2 ,-2, -2, 2]
y1 = [2, -2, -2, 2, 2]
x = np.array(x1)
y = np.array(y1)

def update(frame):
    X = x*np.cos(frame) - y*np.sin(frame)
    Y = y*np.cos(frame) + x*np.sin(frame)
    anim_object.set_data(X, Y)
    return anim_object

ani = FuncAnimation(fig, 
                    update, 
                    frames=np.linspace(0, 4*np.pi, 100),
                    interval=100 
                    )            

ani.save('lec_7_create_animation.gif')