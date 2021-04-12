import numpy as np
a=np.array((5))
for i in range(5):
  print("введите число ")
  a[i]=int(input())
e=0
for i in range(5):
  e=e+a[i]
print(e/5)