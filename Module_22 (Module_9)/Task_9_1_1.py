print('Задача 1. Сисадмин')

import os

folder_name = 'access'
file_name = 'admin.bat'


abs_path = os.path.abspath(os.path.join(folder_name, file_name))
print('Абсолютный путь до файла:', abs_path)

rel_path = os.path.join('..', folder_name, file_name)
print('Относительный путь до файла:', rel_path)