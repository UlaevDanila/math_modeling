import numpy as np 

a=int(input('Введите число'))
n=int(input("Введите степень"))

def func(a, n):
  b=1
  for i in range(0,n):
    b = b*a
  print(b)

func(a,n)