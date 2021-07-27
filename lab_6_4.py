import matplotlib.pyplot as plt
import numpy as np
#from sympy import symbols

def lspiral():
    f = np.arange(0, np.pi*8, np.pi/100, float)
    b = float(input("Введите значение b "))
    r = 2.71**(b*f)
    x = r*np.cos(f)
    y = r*np.sin(f)
    plt.plot(x,y)
    plt.show()
def aspiral():
    f = np.arange(0.01, np.pi*8, np.pi/100, float)
    k = float(input("Введите значение k "))
    r = k*f
    x = r*np.cos(f)
    y = r*np.sin(f)
    plt.plot(x,y)
    plt.show()
def gesl():
    f = np.arange(0, np.pi*8, np.pi/100, float)
    k = float(input("Введите значение k "))
    r = k/(f**(1/2))
    x = r*np.cos(f)
    y = r*np.sin(f)
    plt.plot(x,y)
    plt.show()
def rosa():
    f = np.arange(0, np.pi*8, np.pi/100, float)
    k = float(input("Введите значение k "))
    r = np.sin(k*f)
    x = r*np.cos(f)
    y = r*np.sin(f)
    plt.plot(x,y)
    plt.show()

#lspiral()
#aspiral()
#gesl()
rosa()