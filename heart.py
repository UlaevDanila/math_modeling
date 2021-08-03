import matplotlib.pyplot as plt
import numpy as np

def draw(a):
    x = np.linspace(-10,10,1000)
    y = np.linspace(-10,10,1000)
    X,Y = np.meshgrid(x, y)
    fxya = (np.sin(np.pi*a/10) + X)**2 + (np.cos(np.pi*a/10) + Y)**2 - 7/10*Y*np.abs(X)
    plt.contour(X, Y, fxya, levels=[1])


for i in np.arange(1,19,0.5):
    a = i
    draw(a)

plt.axis('equal')
plt.show()