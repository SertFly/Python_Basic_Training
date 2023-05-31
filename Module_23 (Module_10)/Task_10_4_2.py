print('Задача 2. Логирование')

# Возможно, вы замечали, что некоторые программы не просто выдают ошибку и
# закрываются, но и записывают эту ошибку в файл. Таким образом проще
# сформировать отчёт об ошибках, а значит, программисту будет проще их
# исправить. Это называется логированием ошибок.

# Дан файл words.txt, в котором построчно записаны слова. Необходимо
# определить количество слов, из которых можно получить палиндром
# (привет предыдущим модулям). Если в строке встречается число, то
# программа выдаёт ошибку ValueError и записывает эту ошибку в файл errors.log

import string


def check_palindrome(text):
    return text == text[::-1]


def clear_text(text):
    new_text = text.rstrip()
    new_string = new_text.translate(str.maketrans('', '', string.punctuation))
    new_line = new_string.replace(' ', '')
    print(new_line)
    return new_line.lower()


with open('words.txt', 'r', encoding='utf8') as file, open('errors.log', 'w', encoding='utf8') as log_file:
    count = 0
    line_count = 0
    for line in file:
        line_count += 1
        clear_line = clear_text(line)
        try:
            if clear_line.isalpha():
                count += check_palindrome(clear_line)
            else:
                raise ValueError(f'{line_count} строка не полностью состоит из букв!')
        except ValueError as exc:
            log_file.write(f'\n{line_count} строка не полностью состоит из букв!')

    print(count)
