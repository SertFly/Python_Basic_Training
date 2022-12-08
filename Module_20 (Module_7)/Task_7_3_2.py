print('Задача 2. Словари из списков')

# Создайте два списка, в каждом из которых лежит 10 случайных букв алфавита
# (могут повторяться). Затем для каждого списка создайте словарь из пар
# «индекс — значение» и выведите оба словаря на экран.

import random

list_1 = [random.choice('абвгдеёжзийклмнопрстуфхцчшщъыьэюя') for _ in range(10)]
list_2 = [random.choice('абвгдеёжзийклмнопрстуфхцчшщъыьэюя') for _ in range(10)]

print('Первый список:', list_1)
print('Второй список:', list_2)

dict_1 = {i_index: i_symbol for i_index, i_symbol in enumerate(list_1)}
dict_2 = {i_index: i_symbol for i_index, i_symbol in enumerate(list_2)}

print(dict_1)
print(dict_2)
