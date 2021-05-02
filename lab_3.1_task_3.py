import numpy as np 

print('Введите N')
N=int(input())

print('Введите M')
M=int(input())

a=np.zeros((N,M))
max=np.zeros(M)
for i in range(0,N):
  for j in range(0,M):
    print('Введите число')
    a[i][j]=int(input())

print(a)

for i in range(0,N):
  for i in range(0,M):
    if a[j][i]>max[i]:
      max[i]=a[j][i]

print(max)