import numpy as np 

a=int(input('Введите целое значение: '))
n=int(input('Введите показатнль степени: '))

def func(a,n):
  b=1
  while n>0:
    b = b * a
    n = n - 1
    func(a,n)
  return(b)

print(func(a,n))