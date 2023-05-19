print('Задача 1. Простая программа')

# Напишите программу, которая открывает файл и записывает туда введённую пользователем строку.
# Используйте операторы try except else finally. Обработайте возможные ошибки:
#
# Проблема при открытии файла.
# Нельзя преобразовать данные в целое.
# Неожиданная ошибка.

try:
    text_file = open('text.txt', 'x', encoding='utf-8')
    text_file.write(input('Введите текст: '))

except (FileExistsError, PermissionError) as exc:
    print('Проблемы при открытии файла:', exc, type(exc))
except (TypeError, ValueError) as exc:
    print('Введенные данные не конвертируются в строку.', exc, type(exc))
except RuntimeError as exc:
    print('Упс...', exc, type(exc))

else:
    print('Программа выполнилась без ошибок.')
finally:
    text_file.close()
    print(text_file.closed)
