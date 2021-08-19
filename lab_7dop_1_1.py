import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='r', label='Ball')

def cicloida_move(R, angle_vel, time):
    alpha = angle_vel * (np.pi/180) * time
    x = R*(alpha - (np.sin(alpha)))
    y = R*(1-(np.cos(alpha)))
    return x, y

edge = 20

ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def animate(i):
    ball.set_data(cicloida_move(R=2, angle_vel=10, time=i))


ani = animation.FuncAnimation(fig,
                              animate,
                              frames=360,
                              interval=120
                              )

R = 2
x = R*(np.linspace(0,4*np.pi,100) - (np.sin(np.linspace(0,4*np.pi,100))))
y = R*(1-(np.cos(np.linspace(0,4*np.pi,100))))

plt.axis('equal')
plt.plot(x,y)

ani.save('lab_7dop_1_1.gif')