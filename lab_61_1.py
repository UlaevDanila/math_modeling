import matplotlib.pyplot as plt
import numpy as np

def krivay():
    t = np.arange(-10, 10, 0.1 )
    A = 1
    a = 1
    d = np.pi/2
    B = int(input("Введите значение B "))
    b = 2
    x = A*np.sin(a*t+d)
    y = B*np.sin(b*t)
    plt.plot(x,y)
    plt.show()

krivay()