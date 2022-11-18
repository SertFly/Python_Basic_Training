print('Задача 3. Удаление части')

# На вход в программу подаётся строка, состоящая из прописных и заглавных букв кириллицы.
# Напишите код, который проверяет, каких букв в строке больше, прописных или заглавных.
# Если заглавных букв больше, то сделать все буквы строки заглавными, иначе сделать все
# прописными.

# Подсказка: используйте методы islower() и/или isupper().

text = input('Введите текст: ')
lower_counter = len([1 for symbol in text if symbol.islower() == True])
upper_counter = len([1 for symbol in text if symbol.isupper() == True])
if lower_counter > upper_counter:
    print('Результат:', text.lower())
else:
    print('Результат:', text.upper())
