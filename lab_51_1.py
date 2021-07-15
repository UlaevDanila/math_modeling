from sympy import symbols
from sympy.vector import CoordSys3D
from sympy import sin, cos, trigsimp

N = CoordSys3D('N')

a = 4*N.i + 3*N.j + 8*N.k
b = -2*N.i + 8*N.j + 7*N.k
c = -5*N.i - 6*N.j + 12*N.k

ab = a.dot(b)/(a.dot(a)*b.dot(b))**(1/2)
print(ab)

ac = a.dot(c)/(a.dot(a)*c.dot(c))**(1/2)
print(ac)

bc = b.dot(c)/(b.dot(b)*c.dot(c))**(1/2)
print(bc)