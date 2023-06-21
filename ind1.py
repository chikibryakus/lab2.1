import math

a = float(input("Введите длину меньшего основания: "))
b = float(input("Введите длину большего основания: "))
alpha = float(input("Введите угол при большем основании в градусах: "))

c = math.sqrt(b**2 - a**2/4)
h = c * math.sin(math.radians(alpha))
S = ((a+b)/2)*h

print("Площадь равнобедренной трапеции:", S)