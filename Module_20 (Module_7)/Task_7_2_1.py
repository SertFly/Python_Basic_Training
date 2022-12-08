print('Задача 1. Создание кортежей')

# Заполните один кортеж десятью случайными целыми числами от 0 до 5 включительно.
# Также заполните второй кортеж числами от −5 до 0. Объедините два кортежа, создав
# тем самым третий кортеж. С помощью метода кортежа определите в нём количество
# нулей. Выведите на экран третий кортеж и количество нулей в нём.
import random

first_tuple = tuple(random.randint(0, 5) for _ in range(10))
print('Первый кортеж:', first_tuple)

second_tuple = tuple(random.randint(-5, 0) for _ in range(10))
print('Второй кортеж:', second_tuple)

third_tuple = first_tuple + second_tuple
print('Объединенный кортеж:', third_tuple)
print('Кол-во нулей в объединенном кортеже:', third_tuple.count(0))
