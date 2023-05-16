print('Задача 1. Кубы и квадраты')

# Пользователь вводит числа A и B. Напишите программу, которая генерирует два списка:
# в первом лежат кубы чисел в диапазоне от А до В, во втором — квадраты чисел в этом
# же диапазоне. Выведите списки на экран. Для генерации используйте list comprehensions
# (как и в следующих задачах).

left_border = int(input('\nЛевая граница: '))
right_border = int(input('Правая граница: '))

print(f'\nСписок квадратов чисел в диапазоне от {left_border} до {right_border}:',
      [i ** 2 for i in range(left_border, right_border + 1)])
print(f'Список кубов чисел в диапазоне от {left_border} до {right_border}:',
      [i ** 3 for i in range(left_border, right_border + 1)])