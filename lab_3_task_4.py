import numpy as np 

print('Ввеедите N')
N=int(input())
print('Ввеедите M')
M=int(input())

A=np.ndarray((N,M))
for i in range(0,N):
  for j in range(0,M):
    if i==0 or j==0:
      A[i,j]=np.sin(N*(i+1)+M*(j+1))
      if A[i,j]<0:
        A[i,j]=0
    else:
      A[i,j]=np.sin(N*i+M*j)
      if A[i,j]<0:
        A[i,j]=0

#print(A)