print('Задача 1. Список чётных чисел')

# Пользователь вводит два числа: А и В. Реализуйте код, который генерирует список
# из чётных чисел в диапазоне от А до B. Используйте list comprehensions (как и в
# следующих задачах).

print([x for x in range(int(input('\nВведите первое число: ')),
                        int(input('Введите второе число: ')) + 1)
       if x % 2 == 0])