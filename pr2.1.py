import math
x = float(input("Введите переменнцю x: "))
y = float(input("Введите переменнцю y: "))
z = float(input("Введите переменнцю z: "))
s = 2*math.cos(x - 2/3)/(1/2+math.sin(y)**2)*(1 + z**2/(3-z**2/5))
print(s)