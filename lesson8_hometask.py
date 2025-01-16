"""Реализовать программу с функционалом калькулятора
для операций над двумя числами. Числа и операция
вводятся пользователем с клавиатуры. Использовать
ООП. Использовать обработку исключений."""


def check_zero_value(func):
    def wrapper(a, b):
        try:
            if b == 0:
                raise ZeroDivisionError
        except ZeroDivisionError:
            print("Error: You can't divide by zero")
        else:
            return func(a, b)

    return wrapper


def make_multiplication(a, b):
    return a * b


def make_summ(a, b):
    return a + b


@check_zero_value
def make_division(a, b):
    return a / b


@check_zero_value
def make_floor_division(a, b):
    return a // b


@check_zero_value
def make_modulo(a, b):
    return a % b


def make_exponent(a, b):
    return a ** b


def make_subtraction(a, b):
    return a - b


while True:
    first_val = input("Input first char: ")
    try:
        first_val = float(first_val)
    except ValueError:
        print("Value should be a number, allowed separator is ->  \u00b7 dot.")
    else:
        break

while True:
    operation = input("Input operation | + | - | * | / | // | % | ** |: ")
    try:
        if operation not in '+-/*//%**':
            raise ValueError
    except ValueError:
        print("List of allowed operations is: | + | - | * | / | // | % | ** |")
    else:
        break

while True:
    second_val = input("Input second char: ")
    try:
        second_val = float(second_val)
    except ValueError:
        print("Value should be a number, allowed separator is ->  \u00b7 dot.")
    else:
        break

if operation == '*':
    print(make_multiplication(first_val, second_val))
elif operation == '+':
    print(make_summ(first_val, second_val))
elif operation == '/':
    print(make_division(first_val, second_val))
elif operation == '//':
    print(make_floor_division(first_val, second_val))
elif operation == '%':
    print(make_modulo(first_val, second_val))
elif operation == '**':
    print(make_exponent(first_val, second_val))
elif operation == '-':
    print(make_subtraction(first_val, second_val))
