# # """Задача: Проверка делимости
# # Напишите функцию check_division(a, b), которая:
# # Проверяет делимость числа a на b.
# # Если деление успешно, возвращает результат.
# # Используйте else для вывода сообщения "Деление выполнено успешно!" только если исключений не было."""
# #
# #
# # def check_division(a, b):
# #     try:
# #         c = a / b
# #     except Exception as e:
# #         print(e)
# #     else:
# #         print("Executed successfully")
# #         return c
# #     finally:
# #         print("Finalization message")
# #
# # #check_division(1, 2)
# # #check_division(1, 0)
# #
# # check_division(1, '-1')
#
# """Задача: Проверка ввода
# Напишите функцию check_age(age), которая:
# Принимает возраст.
# Если возраст меньше 0 или больше 120, выбрасывает исключение ValueError с сообщением "Некорректный возраст".
# Если возраст корректный, возвращает сообщение "Возраст принят".
# Добавьте обработку этого исключения в основной программе."""
# from math import sqrt
#
# # def check_age(age):
# #     if not  0 < age < 120:
# #         raise ValueError
# #     else:
# #         print("Executed successfully")
# #
# # try:
# #     print(check_age(121))
# # except ValueError as e:
# #     print("Age error")
#
# """Задача: Проверка корректности данных
# Напишите функцию find_average(numbers), которая:
# Принимает список чисел.
# Использует assert для проверки, что список не пуст (иначе сообщение: "Список не должен быть пустым").
# Возвращает среднее арифметическое."""
#
#
# def find_average(numbers):
#     summ = 0
#     assert (numbers != []), "List of numbers is empty"
#     for number in numbers:
#         summ += number
#     average = summ / len(numbers)
#     return average
#
#
# try:
#     print(find_average([]))
# except AssertionError as e:
#     print(e)
#
#
# def imt_calculation(height, weight):
#     imt = weight / ((height / 100) ** 2)
#     if imt < 16:
#         print("дефицит")
#     elif 16 <= imt <= 18.5:
#         print("недостаточная масса")
#     elif 18.5 <= imt <= 25:
#         print("норма")
#     elif 25 <= imt <= 30:
#         print("избыточная масса")
#     elif 30 <= imt <= 35:
#         print("ожирение 1-й степени")
#     elif imt >= 35:
#         print("ожирение 2-й степени")
#
#
# while True:
#     try:
#         height = int(input("Type your height, cm: "))
#         weight = int(input("Type your weight, kg: "))
#         if height <= 0 or weight <= 0:
#             raise ValueError("Cannot be less or equal 0")
#     except TypeError:
#         print("Input number")
#     except ValueError as e:
#         print(e)
#     else:
#         imt_calculation(height, weight)
#         break
#
#

a=float(input("Type: "))
print(a)