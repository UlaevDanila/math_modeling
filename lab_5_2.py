from sympy import symbols
from sympy import sin,cos,sqrt
from sympy import simplify

x,y,z,a=symbols('x y z a')

a=simplify((x*y**2-2*x*y*z+x*z**2+y**2-2*y*z+z**2)/(x**2-1)*sqrt((1+sin(a)))/(1-sin(a))+sqrt((1-sin(a)))/(1+sin(a)))
print(a)