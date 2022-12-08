print('Задача 3. Различные цифры')

# Напишите программу, которая находит все различные цифры в символьной строке.
# Для решения используйте множество (цифры будут различные, и поиск во множестве
# намного быстрее, чем в списке).

# Подсказка: можно использовать вот такое сравнение '0'<=x<='9'

text = {symbol for symbol in input('Введите строку: ')}
digits = {str(i) for i in range(0, 10)}

print('Различные цифры строки:', ''.join(sorted(digits.intersection(text))))
