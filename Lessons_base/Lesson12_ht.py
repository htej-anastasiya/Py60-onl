"""
Домашнее задание:
1. Класс «Автобус». Класс содержит свойства:
    ● Скорость
    ● Максимальное количество посадочных мест
    ● Максимальная скорость
    ● Список фамилий пассажиров
    ● Флаг наличия свободных мест
    ● Словарь мест в автобусе
Методы:
    ● Посадка и высадка одного или нескольких пассажиров
    ● Увеличение и уменьшение скорости на заданное значение
    ● Операции in, += и -= (посадка и высадка пассажира по фамилии)
"""

class Autobus:

    def __init__(self, max_num_of_seats, max_speed, surnames_lst = None,
                 is_empty_seats = True):
        self.speed = 0
        self.max_num_of_seats = max_num_of_seats
        self.max_speed = max_speed
        self.surnames_lst = []
        self.is_empty_seats = True

    def increase_speed_value_to(self, speed):
         self.speed = min(self.speed + speed, self.max_speed)
         return self.speed

    def decrease_speed_value_to(self, speed):
        self.speed = max(0, self.speed-speed)
        return self.speed

    def get_current_speed_value(self):
        return self.speed

    def take_on_passengers(self, surnames_lst):
        free_seats = self.max_num_of_seats - len(self.surnames_lst)
        if free_seats==0:
            self.is_empty_seats = False
            return self.is_empty_seats
        else:
            for surname in surnames_lst[:free_seats]:
                self.surnames_lst.append(surname)
                self.is_empty_seats = len(self.surnames_lst) < self.max_num_of_seats
            return len(self.surnames_lst)

    def take_off_passengers(self, surnames_lst):
        for surname in surnames_lst:
            self.surnames_lst.remove(surname)
            if len(self.surnames_lst) < self.max_num_of_seats:
                self.is_empty_seats = True
        return len(self.surnames_lst)

    def get_lst_of_passengers(self):
        return self.surnames_lst

    def get_free_seats_status(self):
        if self.is_empty_seats is not True:
            return f'NO seats are vacant'
        return f'"{self.max_num_of_seats - len(self.surnames_lst)}" seats are vacant'





bus = Autobus(3, 120)
print(f'New speed is "{bus.increase_speed_value_to(99)}" km/h')
print(f'New speed is "{bus.increase_speed_value_to(16)}" km/h')
print(f'New speed is "{bus.increase_speed_value_to(50)}" km/h')
print(f'New speed after reduce is "{bus.decrease_speed_value_to(56.7)}" km/h')
print(f'Current speed is "{bus.get_current_speed_value()}" km/h')
print(f'"{bus.take_on_passengers(["Test", "Test1"])}" seats are taken')
print(bus.get_free_seats_status())
print(f'"{bus.take_on_passengers(["Test2", "Test3"])}" seats are taken')
print(bus.get_free_seats_status())
print(f'Passengers surnames list: {bus.get_lst_of_passengers()}')
print(f'"{bus.take_off_passengers(["Test"])}" seats are taken')
print(bus.get_free_seats_status())
print(f'Passengers surnames list: {bus.get_lst_of_passengers()}')
