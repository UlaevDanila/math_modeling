import numpy as np 
import math

t=str(input('Введите тип фигуры'))

def area(t):
  if t=="Прямоугольник":
    a=int(input('Введите длинну '))
    b=int(input("Введите ширину "))
    print ("Площадь равна ",a*b)
  elif t=='Круг':
    a=int(input("Введите радиус "))
    print ("Площадь равна ",math.pi*a**2)
  else:
    a=int(input("Введите длинну высоты "))
    b=int(input("Введите длинну основания "))
    print ("Площадь равна ",1/2*+a*b)

area(t)