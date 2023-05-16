print('Задача 2. Поиск файла 2')

import os
import random


# Как мы помним, скрипты — это просто куча строк текста, хоть они и понятны
# только программисту. Таким образом, с ними можно работать точно так же, как
# и с обычными текстовыми файлами.

# Используя функцию поиска файла из предыдущего урока, реализуйте программу,
# которая находит внутри указанного пути все файлы с искомым названием и
# выводит на экран текст одного из них (выбор можно сгенерировать случайно).

# Подсказка: можно использовать, например, список для сохранения найденного пути.

def find_file(cur_path, file_name):
    all_paths = []
    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        if file_name == i_elem:
            all_paths.append(os.path.abspath(path))
        elif os.path.isdir(path):
            result = find_file(path, file_name)
            if result:
                all_paths.extend(result)

    return all_paths


def check_file_inside(path_to_file):
    file = open(path_to_file, 'r', encoding='utf8')
    for line in file:
        print(line)
    file.close()


all_paths = find_file('..', 'Task_2_1.py')
check_file_inside(random.choice(all_paths))
