print('Задача 2. Всё в одном')

import os

# Ваш друг, который тоже проходит курс Python Basic, поехал с ноутбуком
# в другой город, и там у него случилась беда: его диск пришлось отформатировать,
# а доступ в интернет отсутствует. Остался только телефон с мобильным интернетом.
# Так как со связью (и с памятью) проблемы, друг попросил вас скинуть одним файлом
# все решения и скрипты, которые у вас сейчас есть.

# Напишите программу, которая копирует код каждого скрипта в папке проекта python_basic
# в файл scripts.txt, разделяя код строкой из 40 символов *.

def find_file(cur_path):
    results = open('all_scripts.txt', 'w')
    for i_elem in os.listdir(cur_path):
        if os.path.isfile(i_elem):
            file = open(i_elem, 'r', encoding='utf-8')
            for i_line in file:
                results.write(i_line)
            print('*' for i in range(40))
        elif os.path.isdir(i_elem):
            result = find_file(i_elem)
            if result:
                print('Абсолютный путь к файлу:', result)
    else:
        result = None

    return result


common_dir = os.path.join('..', '..')
results = open('all_scripts.txt', 'w')
