import os

print('Поиск файла')


def find_file(cur_path, file_name):
    print('Переходим в', cur_path)

    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        print('\tСмотрим', path)
        if file_name == i_elem:
            return path
        if os.path.isdir(path):
            print('Это директория')
            result = find_file(path, file_name)
            if result:
                break
    else:
        result = None

    return result


file_path = find_file(os.path.abspath
                      (os.path.join('..', '..', '..', '..', 'learn_work')),
                      'Lesson_9_2_1.py')
if file_path:
    print('Абсолютный путь к файлу:', file_path)
else:
    print('Файл не найден.')
