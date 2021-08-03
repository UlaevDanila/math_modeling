import numpy as np
import sympy
from sympy import symbols
from sympy import solve
import matplotlib.pyplot as plt

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

n = 1,41
l = (2*r**2 - 2*r**2*np.cos(180-2*beta(n)))**(1/2)

x1 = l*np.cos(beta(n))
y1 = l*np.sin(beta(n))

x, y = symbols("x y")

fxy = x**2 + y**2 - r**2
l = r*p
fx = fxy.subs(y,l)
a = solve(fx,x)
x2 = [float(a[0]),x1]
y2 = [l,y1]

k = int(input("Введите число точек "))
x3 = np.linspace(-2*r,2*r,k)
y3 = np.linspace(-2*r,2*r,k)
X,Y = np.meshgrid(x3, y3)
fxy= X**2 + Y**2
plt.axis('equal')
plt.contour(X, Y, fxy, levels=[r**2])
plt.plot([-2*r, x2[0]],[l,l])
plt.plot(x2, y2)
plt.show()