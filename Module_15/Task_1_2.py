print('Задача 2. Очень простая задача')

# У вас есть список numbers. Напишите программу, которая заполняет список числами от 0 до 100 и выводит его на экран.

numbers = []
for i in range(10):
    for j in range(10):
        numbers.append(10*i + j)
        print(10*i + j, end = '\t')
    print()
numbers.append(100)
print(100)

numbers_alternative = []
for i in range(101):
    numbers_alternative.append(i)
print('\n', numbers_alternative)