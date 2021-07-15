import matplotlib.pyplot as plt 
import numpy as np

def parabola():
    x1 = int(input("Введите левую границу интервала "))
    x2 = int(input("Введите правую границу интервала "))
    n = int(input("Введите число точек "))
    x = np.linspace(x1,x2,n)
    a = int(input ("Введите значение a "))
    b = int(input ("Введите значение b "))
    c = int(input ("Введите значение с "))
    y = a*x**2 + b*x + c
    plt.plot(x,y)
    plt.show()
  
parabola ()

def giperbola():
    x1 = int(input("Введите левую границу интервала "))
    x2 = int(input("Введите правую границу интервала "))
    n = int(input("Введите число точек "))
    x = np.linspace(x1,x2,n)
    a = int(input ("Введите значение a "))
    y = a/x
    plt.plot(x,y)
    plt.show()

giperbola()