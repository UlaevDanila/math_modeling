from lec_3_constants import g

def energy(m,v,h):
  E=m*g*h+m*v**2/2
  print(E)

print("Введите массу тела")
m=int(input())

print("Введите начальную скорость тела")
v=int(input())

print("Введите высоту")
h=int(input())

energy(m,v,h)