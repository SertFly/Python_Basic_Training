print('Задача 2. Всё в одном')

import os

# Ваш друг, который тоже проходит курс Python Basic, поехал с ноутбуком
# в другой город, и там у него случилась беда: его диск пришлось отформатировать,
# а доступ в интернет отсутствует. Остался только телефон с мобильным интернетом.
# Так как со связью (и с памятью) проблемы, друг попросил вас скинуть одним файлом
# все решения и скрипты, которые у вас сейчас есть.

# Напишите программу, которая копирует код каждого скрипта в папке проекта python_basic
# в файл scripts.txt, разделяя код строкой из 40 символов *.


def find_file(cur_path, ending):
    all_paths = []
    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        if i_elem.endswith(ending):
            all_paths.append(os.path.abspath(path))
        elif os.path.isdir(path):
            result = find_file(path, ending)
            if result:
                all_paths.extend(result)

    return all_paths


def get_text_from_file(path_to_file):
    file = open(path_to_file, 'r', encoding='utf-8')
    result = ''
    for i_line in file:
        result += i_line
    return result


all_py_files = find_file('..', '.py')

file_result = open('all_scripts.txt', 'w', encoding='utf-8')

for file_path in all_py_files:
    file_result.write(get_text_from_file(file_path))
    file_result.write('\n' * 2 + '*' * 80 + '\n' * 2)
