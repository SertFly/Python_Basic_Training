print('Задача 2. Кратность')
# Пользователь вводит список из N чисел и число K. Напишите код, выводящий на экран сумму
# индексов элементов списка, которые кратны K.

quantity = int(input('Введите количество чисел в списке: '))
divider = int(input('Введите делитель: '))
num_list = []
sum_count = 0
i = 0

for _ in range(quantity):
    num = int(input('Введите число из списка: '))
    num_list.append(num)
print(num_list)

for number in num_list:
    if number % divider == 0:
        print(f'Индекс числа {number} - {i}')
        sum_count += i
    i += 1
print('Сумма индексов:', sum_count)
