import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots() 

anim_object3, = plt.plot([], [], 'o', lw=2) 
anim_object4, = plt.plot([], [], 'o', lw=2) 
xdata, ydata = [], [] 

ax.set_xlim(0, 2*np.pi) 
ax.set_ylim(-4, 4) 

def update(frame):
    x = np.linspace(0,frame,15) 
    y1 = 2*np.sin(3*x)
    y2 = 3*np.sin(4*x)
    anim_object3.set_data(x, y1)
    anim_object4.set_data(x, y2)
    return anim_object3, anim_object4

ani = FuncAnimation(fig, 
                    update, 
                    frames=np.arange(0, 2*np.pi, 0.1),
                    interval=100 
                    )            

ani.save('lab_7dop_2.gif')