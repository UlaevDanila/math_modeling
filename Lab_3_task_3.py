from lec_3_constants import g
import numpy as np
print("Введите x0")
x0=int(input())
print("Введите y0")
y0=int(input())
print("Введите Vx0")
Vx0=int(input())
print("Введите Vy0")
Vy0=int(input())
print("Введите t")
t=int(input())
a=np.zeros((6,3))
for i in range(t+1):
  x=x0+Vx0*i
  y=y0+Vy0*t-g*i**2/2
  a[i,0]=i
  a[i,1]=x
  a[i,2]=y
print(a)