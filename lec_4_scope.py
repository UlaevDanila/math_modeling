x0=10
def move (t):
  x=x0*t
  return x
print(move(3))
a="Good"
def my_func():
  a='Bad'
  print(a)
my_func()
print(a)
def changer(a,b):
  a=2
  b[0]='Good'
x=10
L=[1,2]
changer(x,L)
print(x)
print(L)
L=[1,2]
changer(x,L[:])
print(L)