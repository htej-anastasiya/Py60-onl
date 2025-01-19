import functools

"""Дан список чисел. С помощью map() получить список,
где каждое число из исходного списка переведено в строку.
Пример: на входе – [1, 2, 3], на выходе – [‘1’, ‘2’, ‘3’]"""

numbers = [1, 2, 3, 4]
result = list(map(str, numbers))
print(result)

"""Дан список чисел. С помощью filter() получить список
тех элементов из исходного списка, значение которых
больше 0"""

numbers = [1, 2, 3, 4, -3, -10]
result1 = list(filter(lambda x: x > 0, numbers))
print(result1)

"""Lambda-функции
Задача: Сортировка строк
Дан список строк:
python
Копировать код
words = ["python", "lambda", "functional", "decorator", "comprehension"]
Отсортируйте его по длине строк с помощью lambda в функции sorted."""

words = ["functional", "python", "lambda", "decorator", "comprehension"]
result2 = sorted(words, key=len)
result3 = sorted(words, key=lambda word: len(word))
print(result2)
print(result3)

"""Задача: Генератор множителей
Напишите функцию make_multiplier(factor), которая принимает число factor и возвращает замыкание.
Замыкание принимает одно число и возвращает его произведение на factor."""


def make_multiplier(factor):
    def multiplier(number):
        return number * factor

    return multiplier


number = make_multiplier(6)
print(number)
print(number(7))

"""Задача: Обработка списка чисел
Дан список чисел:
nums = [3, 7, 2, 9, 4, 8]
Выполните следующие операции:
Используя map, создайте список, где каждое число увеличено на 1.
Используя filter, оставьте только числа больше 5.
Используя reduce, вычислите произведение всех оставшихся чисел."""

nums = [3, 7, 2, 9, 4, 8]
list1 = list(map(lambda x: x + 1, nums))
list2 = list(filter(lambda x: x > 5, list1))
result = functools.reduce(lambda x, y: x*y, list2 )

print(list1, list2, result)

"""Задача: Декоратор логирования
Реализуйте декоратор log, который:
Перед выполнением функции выводит сообщение Выполняется функция: {имя функции}.
После выполнения выводит Функция {имя функции} завершена"""

