import sympy
from sympy import symbols
from sympy import sin,cos

p=int(input("Введите значение"))
d=int(input("Введите значение"))

x,a=symbols("x a")

e=2.71

ch = ( e**x + e**(-x) )/2
sh = ( e**x - e**(-x) )/2

e=a*sin(p)/(ch-cos(d))
e=e.subs([x,p])
print(e)


