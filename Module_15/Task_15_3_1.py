print('Задача 1. Текстовый редактор: возвращение')

# Мы продолжаем участвовать в разработке нового текстового редактора и делать жизнь
# обычных пользователей чуть лучше. В этот раз у нас стоит задача сделать фишку с
# поиском и заменой символов в выделенной строчке. Например, человек что-то перечислял
# в тексте, но ошибся и вместо точек с запятой использовал двоеточия. Лингвисты негодуют.

# Пользователь вводит строку S. Напишите программу, которая заменяет в строке все двоеточия
# (:) на точки с запятой (;). Также подсчитайте количество замен и выведите ответ на экран
# (и новую строку тоже). Для решения используйте список.

print('Введите текст для редактирования:')
notes = input()
notes_list = list(notes)
print('Отредактированный текст:')
for sym in notes_list:
    if sym == ':':
        sym = ';'
    print(sym, end='')
