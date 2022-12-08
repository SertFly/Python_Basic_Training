print('Задача 2. Цилиндр')

# Андрей однажды уже писал функции для расчёта площади сферы и объёма шара.
# И теперь для своей курсовой работы ему пришлось связаться с цилиндрами.

# Пользователь вводит два значения: радиус и высоту. Напишите функцию для
# расчёта площади боковой поверхности цилиндра и его полной площади.
# Функция должна возвращать два эти значения. После этого в основной
# программе выводятся оба ответа в две строки.

import math


def cylinder_calculation(radius, height):
    side_square = 2 * math.pi * radius * height
    full_square = side_square + 2 * math.pi * radius ** 2
    return side_square, full_square


radius = float(input('Введите радиус цилиндра: '))
height = float(input('Введите высоту цилиндра: '))

side_square, full_square = cylinder_calculation(radius, height)
print('Площадь боковой поверхности цилиндра:', round(side_square, 2))
print('Полная площадь поверхности цилиндра:', round(full_square, 2))
