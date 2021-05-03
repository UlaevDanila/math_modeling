import numpy as np 

n=int(input("Введите номер числа Фибоначчи "))

def fib(n):
  f=np.zeros(np.absolute(n))
  f[0] = 0
  f[1] = 1
  if n>0:
    for i in range(2,n):
      f[i] = f[i-1] + f[i-2]
    print(f)

  if n<0:
    f[0] = 0
    f[1] = 1
    for i in range(2,np.absolute(n)):
      f[i] = f[i-2] - f[i-1]
    print(f)

fib(n)