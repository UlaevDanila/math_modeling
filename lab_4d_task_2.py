import numpy as np 

n = int(input('Введите номер числа Фибоначчи'))

q = np.zeros((n))
q[0]=0
q[1]=1
def fib(n):
  i=2
  while n>i:
    i=i+1
    q[i]=q[i+1]+q[i+2]
    fib(n)
  return q

 print(fib(n))