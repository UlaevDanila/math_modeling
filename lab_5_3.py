from sympy import symbols
from sympy import solve
from sympy import sin

x=symbols('x')
expr=x**2+x+x**(-1)+x**(-2)-4
a=solve(expr,x)
print(a)

E,e,M=symbols("E e M")
a=e-E*sin(M)-M
a1=a.subs([(e,0.8),(M,9)])
a=solve(a1,E)
print(a)