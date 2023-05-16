print('Задача 2. Содержимое')

import os


path_to_project = os.path.abspath(os.path.join('..', '..', 'Skillbox'))
print('\nСодержание директории', path_to_project)
for i_elem in os.listdir(path_to_project):
    path = os.path.join(path_to_project, i_elem)
    print('\t', path)

