import math

"""Домашнее задание:
1.Программа с классом Sphere для представления сферы в
трёхмерном пространстве.
Реализовать методы:
o Конструктор, принимающий 4 числа: радиус и
координаты центра сферы x, y, z. Если конструктор
вызывается без аргументов, создать объект сферы с
единичным радиусом и центром в начале координат.
Если конструктор вызывается только с радиусом,
создать объект с соответствующим радиусом и центром
в начале координат
o Метод get_volume(), возвращающий число – объем шара,
ограниченного текущей сферой
o Метод get_square(), возвращающий число – площадь
внешней поверхности сферы
o Метод get_radius(), возвращающий число – радиус
текущей сферы
o Метод get_center(), возвращающий кортеж с
координатами центра сферы
o Метод set_radius(radius), который принимает новое
значение радиуса, меняет радиус текущей сферы и
ничего не возвращает
o Метод set_center(x, y, z), который принимает новые
значения для координат центра радиуса, меняет
координаты текущей сферы и ничего не возвращает
o Метод is_point_inside(x, y, z), который принимает
координаты некой точки в трёхмерном пространстве и
возвращает True или False в зависимости от того,
находится ли точка внутри сферы"""


def check_negative_value(function):
    def wrapper(self, *args, **kwargs):
        try:
            if self.radius < 0:
                raise ValueError
        except ValueError:
            return f'Radius is less than 0'
        else:
            result = function(self, *args, **kwargs)
            return result

    return wrapper


class BasicSphere:

    def __init__(self, x=0, y=0, z=0, radius=1):
        self.center_x = x
        self.center_y = y
        self.center_z = z
        self.radius = radius

    @check_negative_value
    def get_volume(self):
        volume = (4 / 3) * math.pi * self.radius ** 3
        return f"Sphere volume is {volume:.2f}"

    @check_negative_value
    def get_square(self):
        sphere_square = 4 * math.pi * self.radius ** 2
        return f"Sphere square is {sphere_square:.2f}"

    def get_radius(self):
        return f"Sphere radius is {self.radius}"

    def get_center(self):
        return f"Center(x, y, z) coordinates are {(self.center_x, self.center_y, self.center_z)}"

    def set_radius(self, radius):
        self.radius = radius

    def set_coordinates(self, x, y, z):
        self.center_x = x
        self.center_y = y
        self.center_z = z

    def is_point_inside(self, x, y, z):
        calculation = pow((x - self.center_x), 2) + pow((y - self.center_y), 2) + pow((z - self.center_z), 2)
        if calculation <= pow(self.radius, 2):
            return f"Points {x, y, z} are inside sphere"
        return f"Points {x, y, z} are outside of sphere"


sphere1 = BasicSphere(1, 1, 1, 3)
print(sphere1.get_radius())
print(sphere1.get_square())
print(sphere1.get_center())
sphere1.set_radius(2)
print(sphere1.get_radius())
sphere1.set_coordinates(3, 3, 3)
print(sphere1.get_center())
print(sphere1.is_point_inside(4,4,4))
print(sphere1.is_point_inside(6,6,6))