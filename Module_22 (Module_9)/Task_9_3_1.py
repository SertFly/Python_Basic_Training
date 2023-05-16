print('Задача 1. Результаты')

import os
import random

# Одному программисту дали задачу для обработки неких результатов тестирования
# двух групп людей. Файл первой группы (group_1.txt) находится в папке task,
# файл второй группы (group_2.txt) — в папке Additional_info.

# На экран нужно было вывести сумму очков первой группы, затем разность очков
# опять же первой группы и напоследок — произведение очков уже второй группы.

# Программист оказался не очень опытным, писал код наобум и даже не стал его
# проверять. И оказалось, этот код просто не работает.

file = open('C:\\learn_work\\task\\group_1.txt', 'r', encoding='utf-8')
summa = 0
diff = 0
for i_line in file:
    info = i_line.split()
    summa += int(info[2])
    diff -= int(info[2])
print('Сумма очков первой группы:', summa)
print('Разность очков первой группы:', diff)

file.close()

file_2 = open('C:\\learn_work\\task\\Additional_info\\group_2.txt', 'r', encoding='utf-8')
compose = 1
for i_line in file_2:
    info = i_line.split()
    compose *= int(info[2])

print('Произведение очков второй группы:', compose)
file_2.close()
