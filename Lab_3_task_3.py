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
t=np.arange(0,t,0.1)
x=x0+Vx0*t
y=y0+Vy0*t-g*t**2/2

a=np.ones((len(t),3))
for i in range(0,len(t),1):
  a[i,0]=t[i]
  a[i,1]=x[i]
  a[i,2]=y[i]
print(a)