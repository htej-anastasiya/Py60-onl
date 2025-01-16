# from random import randint
#
# """TASK 5:
# Программа получает на вход строку – сообщение и
# указание, что нужно сделать: шифровать или дешифровать.
# Реализовать две функции: первая шифрует заданное
# сообщение шифром Цезаря, вторая – расшифровывает. В
# зависимости от выбора пользователя (шифровать или
# дешифровать) вызывается соответствующая функция,
# результат выводится в консоль."""
#
# abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
#        'w', 'x', 'y', 'z']
#
# input_value = input("Type something to \"encrypt\" or \"decrypt\": ").lower()
# what_to_do = input("Type COMMAND \"encrypt\" or \"decrypt\": ").lower()
# shift_index = int(input("Type shift index to start process: "))
#
# if what_to_do == "encrypt":
#     def encrypt_word(input_value):
#         new_word = ''
#         for letter in input_value:
#             if letter == " ":
#                 new_word += letter
#             elif letter in abc:
#                 letter = abc[(abc.index(letter) + shift_index) % len(abc)]  # гуглила часть с % len(abc)
#                 new_word += letter
#             else:
#                 new_word += letter
#         return new_word
#
#
#     encrypted_value = encrypt_word(input_value)
#     print(f'Your encrypted text is: {encrypted_value}')
#
# elif what_to_do == "decrypt":
#     def decrypt_word(some_value):
#         decrypt_word = ''
#         for letter in some_value:
#             if letter == " ":
#                 decrypt_word += letter
#             elif letter in abc:
#                 letter = abc[(abc.index(letter) - shift_index) % len(abc)]
#                 decrypt_word += letter
#             else:
#                 decrypt_word += letter
#         return decrypt_word
#
#
#     original_value = decrypt_word(input_value)
#     print(f'Your decrypted text is: {original_value}')
#
# else:
#     print("Your command was not recognized.")
#
#
# """TASK 8:
# Реализовать функцию, которая находит минимальный и
# максимальный элементы в матрице (матрица M x N). Вывести в
# консоль индексы найденных элементов"""
#
# rows_count = int(input("Type the number of rows: "))
# columns_count = int(input("Type the number of columns: "))
# matrix = []
#
#
# def create_matrix(rows_count, columns_count):
#     for i in range(rows_count):
#         row = []
#         for j in range(columns_count):
#             row.append(randint(0, 100))
#         matrix.append(row)
#     return matrix
#
#
# matrix = create_matrix(rows_count, columns_count)
# print(f'Your matrix is:\n{matrix}')
#
#
# def find_max_value(created_matrix):
#     new_matrix = []
#     for row in created_matrix:
#         row_max = max(row)
#         new_matrix.append(row_max)
#     return max(new_matrix)
#
#
# def find_index_of_max(created_matrix):
#     for index_row in range(len(created_matrix)):
#         row = created_matrix[index_row]
#         for index_column in range(len(row)):
#             value = row[index_column]
#             if find_max_value(created_matrix) == value:
#                 return index_row, index_column
#     return None
#
# print(f'Max value for created matrix is "{find_max_value(matrix)}", index of value is {find_index_of_max(matrix)}')
#
# def find_min_value(created_matrix):
#     new_matrix = []
#     for row in created_matrix:
#         row_min = min(row)
#         new_matrix.append(row_min)
#     return min(new_matrix)
#
#
# def find_index_of_min(created_matrix):
#     for index_row in range(len(created_matrix)):
#         row = created_matrix[index_row]
#         for index_column in range(len(row)):
#             value = row[index_column]
#             if find_min_value(created_matrix) == value:
#                 return index_row, index_column
#     return None
#
#
# print(f'Min value for created matrix is "{find_min_value(matrix)}", index of value is {find_index_of_min(matrix)} ')


alphabet = ['a', 'b', 'c', 'd', 'e', ]
arr = []
shift_index = 0


def prepare_array(alphabet, shift_index):
    for i in range(len(alphabet)):
        a = []
        for j in range(len(alphabet)):
            if a[i] is None:
                a.append(alphabet[j])
            elif a[i] == alphabet[j]:
                shift_index += 1
                a.append(alphabet[j])
            letter = alphabet[(alphabet.index(letter) + shift_index) % len(alphabet)]
            shift_index += 1
        arr.append(a)
    return arr


def print_matrix_beautifully(matrix, rows):
    for i in range(rows):
        print(matrix[i])


array = prepare_array(alphabet, shift_index)
print(print_matrix_beautifully(array, 24))
# print(type(alphabet[3]), alphabet[3])