import matplotlib.pyplot as plt
import numpy as np

def circle(r=10):
    n = int(input("Введите число точек "))
    x = np.linspace(-2*r,2*r,n)
    y = np.linspace(-2*r,2*r,n)
    X,Y = np.meshgrid(x, y)
    fxy= X**2 + Y**2
    plt.contour(X, Y, fxy, levels=[r**2])
    plt.show()

def ellipse():
    a = int(input ("Введите значение a "))
    b = int(input ("Введите значение b "))
    n = int(input("Введите число точек "))
    x = np.linspace(-a,a,n)
    y = np.linspace(-b,b,n)
    X,Y = np.meshgrid(x, y)
    fxy = X**2/a + Y**2/b - 1
    plt.contour(X, Y, fxy, levels=[0])
    plt.show()

#circle()
ellipse()