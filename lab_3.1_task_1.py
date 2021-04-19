import numpy as np
import random as rnd

A=np.zeros((4,3))
B=np.zeros((4,3))
C=np.zeros((4,3))

for i in range(0,4):
  for j in range(0,3):
    A[i,j]=rnd.randint(0,100)
for i in range(0,4):
  for j in range(0,3):
    B[i,j]=rnd.randint(0,100)

print(A)
print("")
print(B)
print("")


for i in range(0,4):
  for j in range(0,3):
    if A[i,j]>B[i,j]:
      C[i,j]=A[i,j]
    else:
      C[i,j]=B[i,j]
print(C)