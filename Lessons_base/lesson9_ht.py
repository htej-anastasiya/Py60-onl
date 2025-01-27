from datetime import datetime
from xml.etree.ElementTree import indent

import json
import os
import csv

"""
Topics: модуль os. Работа с файлами. Сериализация и десериализация
Работа с внешними данными: JSON, CSV. Регулярные выражения

Исходные данные:
https://drive.google.com/drive/folders/1KH3pJewo3QKl3mua2XnJDv9xN2LxusbE?usp=sharing
Пункты задания:
0. Есть данные в формате JSON – взять с диска с исходными данными.
1. Реализовать функцию, которая считает данные из исходного JSON-файла и преобразует их в формат CSV
2. Реализовать функцию, которая сохранит данные в CSV-файл (данные должны сохраняться независимо от их
количества – если добавить в исходный JSON-файл ещё одного сотрудника, работа программы не должна нарушаться).
3. Реализовать функцию, которая добавит информацию о новом сотруднике в JSON-файл. Пошагово вводятся все
необходимые данные о сотруднике, формируются данные для записи.
4. Такая же функция для добавления информации о новом сотруднике в CSV-файл.
5. Реализовать функцию, которая выведет информацию об одном сотруднике по имени. Имя для поиска вводится с клавиатуры.
6. Реализовать функцию фильтра по языку: с клавиатуры вводится язык программирования, выводится список всех
сотрудников, кто владеет этим языком программирования.
7. Реализовать функцию фильтра по году: ввести с клавиатуры год рождения, вывести средний рост всех
сотрудников, у которых год рождения меньше заданного.
8. Программа должна представлять собой интерактив – пользовательское меню с возможностью выбора
определённого действия (действия – функции из предыдущих пунктов + выход из программы). Пока
пользователь не выберет выход из программы, должен предлагаться выбор следующего действия
"""
FOLDER = "json"
FILE = "data.json"


def convert_from_json_to_python_object(folder, file):
    with open(os.path.join(folder, file), "r") as json_file:
        data_dict = json.load(json_file)
        return data_dict


def write_new_info_into_json(folder, file, updated_obj):
    with open(os.path.join(folder, file), "w") as json_file:
        json.dump(updated_obj, json_file, indent=2)


def add_data_into_json(folder, file):
    object_converted = convert_from_json_to_python_object(folder, file)
    object_converted.append(start_user_input())
    write_new_info_into_json(folder, file, object_converted)


def start_user_input():
    while True:
        try:
            name = input("Input your name: ")
        except ValueError:
            print("Value name has incorrect input, please try again.")
        else:
            break

    while True:
        try:
            birthday_raw = input("Input your birthday date in this format: DD.MM.YYYY: ")
            birthday = datetime.strptime(birthday_raw, "%d.%m.%Y").strftime("%d.%m.%Y")
        except ValueError:
            print("Incorrect data format, should be  DD.MM.YYYY, please try again.")
        else:
            break

    while True:
        height_raw = input("Input your height (in cm): ")
        try:
            height = float(height_raw)
        except ValueError:
            print("Value should be a number, allowed separator is ->  \u00b7 dot.")
        else:
            break

    while True:
        weight_raw = input("Input your weight (in kg): ")
        try:
            weight = float(weight_raw)
        except ValueError:
            print("Value should be a number, allowed separator is ->  \u00b7 dot.")
        else:
            break

    while True:
        car_raw = input("Do you have a car? (Y/N): ")
        try:
            if car_raw.lower() in ["y", "yes"]:
                car = True
            else:
                car = False
        except ValueError:
            print("Incorrect input, value should be Y or N, please try again.")
        else:
            break

    while True:
        languages_raw = input("Which programming language do you know?: ").capitalize()
        try:
            languages = languages_raw.split(" ")
        except ValueError:
            print("Incorrect input, allowed separator is ->  \u00b7 space, please try again.")
        else:
            break

    manual_input_dict = {
        "name": name,
        "birthday": birthday,
        "height": height,
        "weight": weight,
        "car": car,
        "languages": languages
    }
    return manual_input_dict


def convert_json_to_csv(json):
    converted_json = []
    for json_item in json:
        new_json_item = {
            "name": json_item["name"],
            "birthday": json_item["birthday"],
            "height": json_item["height"],
            "weight": json_item["weight"],
            "car": json_item["car"],
            "languages": ", ".join(json_item["languages"])
        }
        converted_json.append(new_json_item)
    with open("base_file.csv", mode="w", encoding="utf-8") as csv_file:
        names = converted_json[0].keys()
        file_writer = csv.DictWriter(csv_file, delimiter=",", fieldnames=names)
        file_writer.writeheader()
        file_writer.writerows(converted_json)
    return converted_json


def search_employee_by_name(json_file):
    employee_name = input("Input employee name: ")
    for person_info in json_file:
        if employee_name in person_info["name"]:
            return person_info


def search_by_prog_lang(json_file):
    prog_lang = input("Input programming language to find employees with such technology: ").capitalize()
    employees_list = []
    for person_info in json_file:
        if prog_lang in person_info["languages"]:
            employees_list.append(person_info["name"])
        else:
            "Not found"
    return employees_list


def search_by_year(json_file):
    birth_year = int(input("Input birth year to find average height of found employees: "))
    employees_height_list = []
    for person_info in json_file:
        if "birthday" in person_info:
            birth_date = datetime.strptime(person_info["birthday"], "%d.%m.%Y")
            if birth_date.year <= birth_year:
                employees_height_list.append(person_info["height"])
            else:
                "Not found"
    average_height = sum(employees_height_list) / len(employees_height_list)
    return average_height

"""8. Программа должна представлять собой интерактив – пользовательское меню с возможностью выбора
определённого действия (действия – функции из предыдущих пунктов + выход из программы). Пока
пользователь не выберет выход из программы, должен предлагаться выбор следующего действия"""


def main_menu():
    while True:
        print("""Available functions:
                                            1 - Deserialize a JSON file
                                            2 - Convert a JSON file to a CSV file
                                            3 - Add a person to a JSON file
                                            4 - Add a person to a CSV file
                                            5 - Find an employee by name
                                            6 - Find a list of employees who know a specific programming language
                                            7 - Calculate the average height of employees
                                            8 - Exit the program
                                            """)
        select_option = int(input("Please enter the number that corresponds to the option you want to perform: "))
        if select_option == 1:
            print(convert_from_json_to_python_object(FOLDER, FILE))
        elif select_option == 2:
            json_file = convert_from_json_to_python_object(FOLDER, FILE)
            print(convert_json_to_csv(json_file))
        elif select_option == 3:
            add_data_into_json(FOLDER, FILE)
            print("Data was added into json")
        elif select_option == 4:
            add_data_into_json(FOLDER, FILE)
            json_file = convert_from_json_to_python_object(FOLDER, FILE)
            convert_json_to_csv(json_file)
            print("Data was added into csv")
        elif select_option == 5:
            search_name = convert_from_json_to_python_object(FOLDER, FILE)
            result = search_employee_by_name(search_name)
            if result is not None:
                print("Employee found:", result)
            else:
                print("Employee not found")
        elif select_option == 6:
            json_file = convert_from_json_to_python_object(FOLDER, FILE)
            result = search_by_prog_lang(json_file)
            if result != "Not found":
                print("The list of employees:", result)
            else:
                print("Nothing was found")
        elif select_option == 7:
            json_file = convert_from_json_to_python_object(FOLDER, FILE)
            result = search_by_year(json_file)
            if result != "Not found":
                print("The average height is, cm:", result)
            else:
                print("Nothing was found")
        elif select_option == 8:
            print("Exited menu")
            break
        else:
            print("Command not found")

main_menu()