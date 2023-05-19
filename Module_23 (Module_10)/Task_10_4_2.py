print('Задача 2. Логирование')

# Возможно, вы замечали, что некоторые программы не просто выдают ошибку и
# закрываются, но и записывают эту ошибку в файл. Таким образом проще
# сформировать отчёт об ошибках, а значит, программисту будет проще их
# исправить. Это называется логированием ошибок.

# Дан файл words.txt, в котором построчно записаны слова. Необходимо
# определить количество слов, из которых можно получить палиндром
# (привет предыдущим модулям). Если в строке встречается число, то
# программа выдаёт ошибку ValueError и записывает эту ошибку в файл errors.log


def check_palindrom(text):
    counts = {}
    for symbol in text:
        if symbol in counts.keys():
            counts[symbol] += 1
        elif symbol in 'abcdefghijklmnopqrstuvwxyz' or symbol in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
            counts[symbol] = 1

    middle_point = ''  # только одна буква может встречаться нечетное количество раз
    for symbol in counts:
        if middle_point and counts[symbol] % 2 == 1:
            return False
        elif counts[symbol] % 2 == 1:
            middle_point = symbol
    return True

