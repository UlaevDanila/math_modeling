import numpy as np

p = float(input("Введите значение прицельного параметра "))
r = float(input("Введите радиус окружности "))

def alpha(p,r):
    a = np.arctan(p/((r**2-p**2)**(1/2)))
    return a

def beta(n):
    sinb = np.sin(alpha(p,r))/n
    b = np.arctan(sinb/((1-sinb**2)**(1/2)))
    return b

def fi(beta, alpha):
    f = 4*beta(n) - 2*alpha(p,r)
    return f
