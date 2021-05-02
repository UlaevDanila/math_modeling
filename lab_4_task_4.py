import numpy as np 

print('Введите a')
a=int(input())

print('ВВедите b')
b=int(input())

print('Введите количество точек')
n=int(input())

def func(a,b,n): 
  q=np.zeros((n,2))
  print(q)
  for j in range(0,n):
    for i in np.arange(a+(a-b)/n,b-(a-b)/n,(a-b)/n):
      q[j][0]=i 
      q[j][1]=i**2
  print(q)

func(a,b,n)