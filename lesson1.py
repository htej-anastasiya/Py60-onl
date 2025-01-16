"""
Деление нацело.
Она отличается от обычного деления тем, что ответ всегда будет целого типа
36 // 11 -> 3
Остаток от деления.
Она обозначается знаком процента %
19 % 7 -> 5 или 7*2+5(остаток), 2 % 7 -> 7 умещается в 2 0 раз, остаток будет 2
Функция pow - позволяет выполнить операцию возведения в степень.
Она принимает на вход два числа и возводит первое из них в степень второго.
pow(2,3) -> 8 или 2**3 -> 8
"""

# print ((a**2+b**2)**0.5)
#
# string = 'Hello world'
# string2 =  'a b c'
# string3 = 'test'
# string4 ='test1 test2 test3 test4 test5'
# print(len(string.split(' ')))
# print(len(string2.split(' ')))
# print(len(string3.split(' ')))
# print(len(string4.split(' ')))
#
#
# a = 'hhhabchghhh'
# b=a[1:-1]
# print(b)
# print(b.replace('h','H'))
#
# test = 'Hello'
# print(test[2])
# print(test[-2])
# print(test[:5])
# print(test[:-2])
# print(test[::2])
# print(test[1::2])
# print(test[::-1])
# print(test[::-2])

""" Дано целое число. Выведите его последнюю цифру.
Например, дано 200 - последняя цифра 0. Дано 123 - последняя
цифра 3. Дано 587 - последняя 7 """
input_value = input("Type digit: ")
last_symbol = input_value[-1]
print(f'Дано {input_value} - последняя {last_symbol}')


""" Дано трехзначное число, найти количество его десятков.
Например, дано 123 – количество десятков: 2, дано 978 –
количество десятков: 7 """
input_value = int(input("Type digit: "))
number_of_tens = (input_value // 10) % 10
print(f'Дано {input_value} - количество десятков {number_of_tens}')


"""Дано трехзначное число, найти сумму его цифр. Например,
дано 123 – сумма 6, дано 555, сумма 15"""

input_value = input("Type something: ")
splitted_values =list(input_value)
new_val=0
for digit in splitted_values:
    new_val +=int(digit)
print(f'дано {input_value} - сумма {new_val}')