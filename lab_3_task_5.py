from lab_3_task_4 import A,N,M
import numpy as np 

print('Введите первый номер')
a=int(input())
print('Введите второй номер')
b=int(input())

m=np.zeros((N))
n=np.zeros((N))
print(A)
for i in range(0,N):
  m[i]=A[i,a]
  n[i]=A[i,b]
for i in range(0,N):
  A[i,a]=n[i]
  A[i,b]=m[i]

print(A)