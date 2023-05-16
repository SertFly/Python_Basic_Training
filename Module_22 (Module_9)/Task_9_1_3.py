print('Задача 3. Корень диска')

import os

get_path = os.path.abspath('..')
print('Текущая папка:', get_path)
print('Корень диска:', os.path.join(get_path.split(os.path.sep)[0]) + os.path.sep)

