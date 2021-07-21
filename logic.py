import sympy
from sympy import symbols
from sympy import solve
from angles import r, p
import numpy as np

x, y = symbols("x y")

fxy = x**2 + y**2 - r**2
fx = fxy.subs(y,p)
a = solve(fx,x)

for i in range(0, len(a), 1):
  if a[i] > 0:
    root = a 

x = np.linspace(-2*r, root, 3)
y = np.zeros([len(x)])

for i in range(0, len(y), 1):
  root = y[i]

