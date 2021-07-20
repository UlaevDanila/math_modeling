import matplotlib.pyplot as plt
import numpy as np

def elipse():
    f = np.arange(0, np.pi*8, np.pi/100, float)
    p = float(input("Введите значение p "))
    e = float(input("Введите значение e "))
    r = p/(1+e*np.cos(f))
    x = r*np.cos(f)
    y = r*np.sin(f)
    plt.plot(x,y)
    plt.show()

elipse()