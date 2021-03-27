print('Введите первую сторону')
a=int(input())
print('Введите вторую сторону')
b=int(input())
print('Введите третью сторону')
c=int(input())
if a+b<c or a+c<b or b+c<a:
  print('существует')
else:
  print('не существует')
if a==b==c:
  print('равносторонний')
if a==b or a==c or b==c:
  print('равнобедренный')
