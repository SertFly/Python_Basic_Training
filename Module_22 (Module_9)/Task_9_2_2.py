print('Задача 2. Поиск файла')

import os


# В уроке мы написали функцию, которая ищет нужный нам файл во всех подкаталогах
# указанной директории. Однако, как мы понимаем, файлов с таким названием может
# быть несколько.

# Напишите функцию, которая принимает на вход абсолютный путь до директории и имя
# файла, проходит по всем вложенным файлам и папкам и выводит на экран все абсолютные
# пути с этим именем.

def find_file(cur_path, file_name):

    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        if file_name == i_elem:
            return path
        if os.path.isdir(path):
            result = find_file(path, file_name)
            if result:
                print('Абсолютный путь к файлу:', result)
    else:
        result = None

    return result


common_dir = input('Введите область для поиска: ')
file_name = input('Введите имя файла: ')

file_path = find_file(common_dir, file_name)