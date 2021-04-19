import numpy as np 

a=np.zeros(5)
q=np.zeros(5)

for i in range(0,4):
  print("Введите значение")
  a[i]=int(input())


q=tuple(a)

print(q)

print("Введите число")
b=int(input())

print("Введите его позицию")
c=int(input())

for i in range(c-1,4):
  a[c-1]=b
  a[i-1]=q[i]
  if i==4 and c==5:
    a[c]=b

print(a)