from sympy import symbols
from sympy.vector import CoordSys3D
from sympy import sin, cos, trigsimp

N = CoordSys3D('N')
q1, q2, x, y, z = symbols("q1 q2 x y z")

E1 = q1*x/((x**2+y**2+z**2)**(3/2))*N.i+ q1*y/((x**2+y**2+z**2)**(3/2))*N.j + q1*z/((x**2+y**2+z**2)**(3/2))*N.k
E2 = q2*(x-1)/((x**2+y**2+z**2)**(3/2))*N.i+ q2*(y-1)/((x**2+y**2+z**2)**(3/2))*N.j + q2*(z-1)/((x**2+y**2+z**2)**(3/2))*N.k

a=E1+E2
E=a.subs([(q1,1),(q2,-0.5),(x,3),(y,4),(z,5)])
print(E)

result=(E.dot(E))**(1/2)
print(result)