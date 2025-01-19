import random

""" я решила еще перед ДЗ добавить мои решения задачек, 
которые были в конце занятия, с которого пришлось уйти
(решала сама, потом посмотрела как на зянятии делали)"""

"""Игра: Четное или нечетное
Условие:
Запросите у пользователя число.
Если число четное, выведите: "Число четное".
Если число нечетное, выведите: "Число нечетное"."""

# input_number = int(input("Type a number:"))
# if input_number % 2 == 0:
#     print(input_number, "is an even number.")
# else:
#     print(input_number, "is an odd number.")

"""Сумма чисел
Условие:
Запросите у пользователя число N.
Вычислите сумму всех чисел от 1 до N (включительно) с использованием цикла for.
Выведите результат."""

# input_number = int(input("Type a number:"))
# new_number = 0
# for i in range(input_number + 1):
#     new_number += i
# print(new_number)

"""Угадай число
Условие:
Компьютер загадывает случайное число от 1 до 100 (используйте random.randint).
Пользователь должен угадать число, вводя варианты.
Если введенное число больше загаданного, выведите: "Меньше".
Если меньше, выведите: "Больше".
Цикл продолжается, пока пользователь не угадает число.
Дополнительно: Добавьте счетчик попыток и выведите его по завершении игры.
Реализуйте выход из игры по команде "выход"."""

# random_number = random.randint(1, 100)
# # print(random_number)
# user_input = input("Input number from 1 to 100 or \"exit\" to quit: ")
# try_number = 1
# while True:
#     if user_input == "exit":
#         break
#     elif int(user_input) != random_number and int(user_input) > random_number:
#         print(f"input smaller value than {user_input}")
#         user_input = input("Input number from 1 to 100 or \"exit\" to quit: ")
#         try_number += 1
#     elif int(user_input) != random_number and int(user_input) < random_number:
#         print(f"input larger value, than {user_input}")
#         user_input = input("Input number from 1 to 100 or \"exit\" to quit: ")
#         try_number += 1
#     else:
#         print(f"You guessed right! The number is {user_input}. Your number of tries is {try_number}")
#         break

# HOMEWORK
"""Маша хочет накопить на телефон, который стоит N денег.
Маша может откладывать k рублей каждый день, кроме
воскресенья (в воскресенье она тратит эти деньги на поход в
кино). Маша начинает копить в понедельник. За сколько дней
она накопит нужную сумму?"""

phone_price = int(input("Type a phone price: "))
savings_amount_per_day = int(input("Type a savings amount per day: "))
savings_total = 0
day_number = 0  # First day of the week
while savings_total <= phone_price:
    day_number += 1
    if day_number % 7 == 0:
        continue
    else:
        savings_total += savings_amount_per_day
print(f'To save {phone_price} you need to spend next amount of days: {day_number - 1}')

"""Реализовать вывод последовательности чисел Фибоначчи
(1 1 2 3 5 8 13 21 34 55 89 ...), где каждое следующее число
является суммой двух предыдущих."""

# fib_num1 = int(input("Type first Fibonacci number: "))
# fib_num2 = int(input("Type second Fibonacci number: "))
# quantity_of_fib_numbers = int(input("How many numbers to show in a row: "))
#
# fibonacci_numbers_row = [fib_num1, fib_num2]
# for i in range(2, quantity_of_fib_numbers):
#     fibonacci_numbers_row.append(fibonacci_numbers_row[i - 1] + fibonacci_numbers_row[i - 2])
# print(f'Your Fibonacci sequence is {fibonacci_numbers_row}')

