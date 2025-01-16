"""Используя модуль math, вычислите значения по следующим
формулам"""
from math import cos, sin, pow, sqrt, pi

x = int(input("Type number: "))
y = pow((pow(cos(x ** 2), 2) + pow(sin(2 * x - 1), 2)), (1 / 3))
print(y)

x = int(input("Type number: "))
y = (5 * x) + (3 * pow(x, 2) * sqrt(1 + pow(sin(x), 2)))
print(y)

"""
«Интерстеллар»
L - длина года на планете
R – радиус орбиты планеты (млн. км.)
𝑣 – орбитальная скорость (км/ч)
Пользователь вводит с клавиатуры информацию о двух планетах:
радиус и орбитальную скорость. Программа должна посчитать и
вывести длину года на первой и второй планетах, а также вывести,
правда ли, что на первой планете год длиннее, чем на второй.
Сделать ввод/вывод данных красивым интерактивом """

radius1, radius2 = input("Type radiuses for planet one and two via SPACE, mln.km: ").split()
orbital_velocity1, orbital_velocity2 = input("Type orbital velocity for planet one and two via SPACE, km/h: ").split()

l1 = (2 * int(radius1) * pi) / int(orbital_velocity1)
l2 = (2 * int(radius2) * pi) / int(orbital_velocity2)

if l1 > l2:
    print(f'planetary year length of planet one "{round(l1, 2)}" is bigger than planet two "{round(l2, 2)}"')
else:
    print(f'planetary year length of planet one "{round(l1, 2)}" is smaller than planet two "{round(l2, 2)}"')
