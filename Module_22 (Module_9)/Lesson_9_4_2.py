import os


def find_file(cur_path, file_name):
    print('Переходим в', cur_path)
    all_paths = []
    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        print('\tСмотрим', path)
        if file_name == i_elem:
            all_paths.append(os.path.abspath(path))
        if os.path.isdir(path):
            print('Это директория')
            result = find_file(path, file_name)
            if result:
                all_paths.extend(result)

    return all_paths


file_path = find_file(os.path.abspath
                      (os.path.join('..', '..', '..', '..', 'learn_work')),
                      'Task_2_1.py')
history_file = open('search_history.txt', 'a')

if file_path:
    for i_file in file_path:
        history_file.write('\n' + i_file)
        print('Абсолютный путь к файлу:', i_file)
else:
    print('Файл не найден.')
