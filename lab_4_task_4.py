import numpy as np 

a=int(input('Введите a: '))
b=int(input('Введите b'))
n=int(input('Введите количество точек'))

def func(a, b, n):

  q = np.linspace(a, b, n)
  w = np.zeros((len(q), 2))

  for i in range(0, len(q)):
    w[i][0] = q[i]
    w[i][1] = q[i]**2
 
  print(w)

func(a, b, n)  