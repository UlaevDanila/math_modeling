print("Ввдеите первое число")
a=int(input())
print("Ввдеите второе число")
b=int(input())
if b!=0:
    if a%b==0 and b!=0:
        print(f"{a} делится на {b}")
        print('a/b= ',a/b)
    else:
        print(f'{a} не делится на {b}')
        print("a/b= ",a//b)
        print('Остаток от деления равен ',a%b)
else:
    print('На ноль делить нельзя')