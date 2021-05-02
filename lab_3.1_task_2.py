import numpy as np 

a=np.zeros(5)
q=np.zeros(4)

for i in range(0,4):
  print('Введите значение')
  q[i]=int(input())

q=tuple(q)

print('Введите элемент')
r=int(input())
print("Введите его номер")
w=int(input())

print(q)

for j in range(0,w-1,1):
  a[j]=q[j]
a[w-1]=r

for i in range(w,5):
  a[i]=q[i-1]

print(a)