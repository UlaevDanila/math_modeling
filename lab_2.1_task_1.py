print('Введите первый коэффициент')
a=int(input())
print('Введите второй коэффициент')
b=int(input())
print('Введите третий коэффициент')
c=int(input())
D=b**2-4*a*c
if D>0:
  x1=(-b-D*(1/2))/2*a
  print(f'x1={x1}')
  x2=(-b+D*(1/2))/2*a
  print(f'x2={x2}')
elif D==0:
  x1=(-b)/2*a
  print(f'x1,2={x1}')
else:
  print('Нет корней')