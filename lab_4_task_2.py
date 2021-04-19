import numpy as np 

def sr(a):
  b=1
  for i in range(0,len(a)):
    b=b*a[i]
  print(b)

b=np.zeros(6)

for i in range(0,len(b)):
  print("Введите значение")
  b[i]=int(input())

sr(b)