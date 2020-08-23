# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой —
# цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их
# как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера:
# [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
import collections
from functools import reduce


def interpreter_in_hex(number):
    result = []
    while number > CONSTANT:
        a = number // CONSTANT
        b = number - a * CONSTANT
        number = a
        result.append(dict_dec[b])
    else:
        result.append(dict_dec[number])
    return result[::-1]


CONSTANT = 16
N = 2  # int(input('Введите целым числом колличестов шестнадцатиричных чисел, которые надо сложить/перемножить: '))

dict_dec = {
    0: '0', 1: '1', 2: '2', 3: '3',
    4: '4', 5: '5', 6: '6', 7: '7',
    8: '8', 9: '9', 10: 'A', 11: 'B',
    12: 'C', 13: 'D', 14: 'E', 15: 'F'
}

dict_hex = {
    '0': 0, '1': 1, '2': 2, '3': 3,
    '4': 4, '5': 5, '6': 6, '7': 7,
    '8': 8, '9': 9, 'A': 10, 'B': 11,
    'C': 12, 'D': 13, 'E': 14, 'F': 15
}

hex_numbers = collections.defaultdict(list)
for i in range(N):
    number = input(f'Введите {i + 1}-е шестнадцатиричное число: ')
    for j in number:
        hex_numbers[i].append(j)

sum_or_mul = []
for n in range(N):
    standard_number = 0
    degree = len(hex_numbers[n]) - 1
    for x in range(len(hex_numbers[n])):
        standard_number += dict_hex[hex_numbers[n][x]] * CONSTANT ** degree
        degree -= 1
    sum_or_mul.append(standard_number)

my_sum = sum(sum_or_mul)
my_mul = reduce(lambda x1, x2: x1 * x2, sum_or_mul)  # на случай если чисел будет больше двух
# my_mul = sum_or_mul[0] * sum_or_mul[1]

print(f'Сумма введённых чисел равна: {interpreter_in_hex(my_sum)}')
print(f'Произведение введённых чисел равно: {interpreter_in_hex(my_mul)}')
