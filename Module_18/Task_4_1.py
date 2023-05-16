print('Задача 1. Шифр Цезаря 2')

# Мы уже писали программу, которая шифрует строку с помощью шифра Цезаря.
# Напомним, что в таком способе шифрования каждая буква заменяется на
# следующую по алфавиту через K позиций по кругу.

# Напишите (модифицируйте) программу, которая реализует этот алгоритм
# шифрования. Не используйте конкатенацию и сделайте так, чтобы текст
# был в одном регистре.

text = input('\nВведите текст: ')
shift = int(input('Введите сдвиг: '))

alphabet = [chr(index) for index in range(ord('а'), ord('я') + 1)]  # заполняем список буквами алфавита

new_text = [alphabet[(alphabet.index(symbol) + shift) % len(alphabet)] if symbol in alphabet
            else symbol for symbol in text.lower()]
print(''.join(new_text))  # объединяем без пробелов
