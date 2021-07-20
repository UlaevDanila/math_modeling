import matplotlib.pyplot as plt
import numpy as np
from sympy import solve
from sympy import symbols

r = float(input("Введите радиус окружности "))

x, y = symbols("x y")
a = x**2+(y-1)**2 - r**2
b = x**2
a1 = a.subs(y,b)
a = solve(a1,x)
print(a)
n = int(input("Введите число точек "))

x = np.linspace(-2*r,2*r,n)
y = x**2

y2 = np.zeros([len(a)])
for i in range(0, len(a), 1):
    y2[i] = a[i]**2

y1 = np.linspace(-2*r,2*r,n)
X,Y = np.meshgrid(x, y1)
fxy= X**2 + (Y-1)**2

plt.plot(x,y)
plt.contour(X, Y, fxy, levels=[r**2])
for i in range(0, len(a), 1):
    plt.plot(a[i], y2[i], marker="*", color="r")
plt.axis("equal")
plt.show()

