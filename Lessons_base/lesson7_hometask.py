import time
from functools import reduce

"""
    Сделать декоратор, который измеряет время,
затраченное на выполнение декорируемой функции.
   Используя map() и reduce() посчитать площадь
квартиры, имея на входе характеристики комнат квартиры.
Пример входных данных:
rooms = [
{"name": ”Kitchen", "length": 6, "width": 4},
{"name": ”Room 1", "length": 5.5, "width": 4.5},
{"name": ”Room 2", "length": 5, "width": 4},
{"name": ”Room 3", "length": 7, "width": 6.3},
"""

rooms = [
    {"name": "Kitchen", "length": 6, "width": 4},
    {"name": "Room 1", "length": 5.5, "width": 4.5},
    {"name": "Room 2", "length": 5, "width": 4},
    {"name": "Room 3", "length": 7, "width": 6.3}
]


def time_decorator(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        some_function = function(*args, **kwargs)
        end_time = time.time()
        delta_time = end_time - start_time
        print(f'Function execution time is {delta_time:.6f} seconds')
        return some_function

    return wrapper


@time_decorator
def count_square(array):
    rooms_square = list(map(lambda i: i["length"] * i["width"], array))
    object_square = reduce(lambda i,j: i*j, rooms_square)
    print(f'Your object square is {object_square} m2')
    return rooms_square


count_square(rooms)
