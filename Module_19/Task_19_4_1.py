print('Задача 1. Пунктуация')

punctuation_set = set('.,;:!?')

text = input('Введите текст: ')
count = 0

for symbol in text:
    if symbol in punctuation_set:
        count += 1
print('Количество знаков пунктуации:', count)