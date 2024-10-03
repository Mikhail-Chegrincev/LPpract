import math
x = float(input("Введите переменнцю x: "))
y = float(input("Введите переменнцю y: "))
z = float(input("Введите переменнцю z: "))
s = (y+(x-1)**1/3)**1/4/abs(x-y)/(math.sin(z)**2+math.tan(z))
print(s)